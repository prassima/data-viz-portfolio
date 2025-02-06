from pandas_gbq import read_gbq
import pandas

query = """
select unique_session_id, device, engaged_session, event_timestamp as view_timestamp, page_location_clean as page_viewed, 
rank() over (partition by unique_session_id order by event_timestamp) as page_order, 
lead(page_location_clean) over (partition by unique_session_id order by event_timestamp) as next_page_viewed,
if(rank() over (partition by unique_session_id order by event_timestamp) = 1,1,0) as entrance, 
if(lead(page_location_clean) over (partition by unique_session_id order by event_timestamp) is null,1,0) as exit

from 

(
select 
-- adding in user first touch timestamp as a failsafe when the user_id is null.
  CONCAT(COALESCE(user_pseudo_id,cast(user_first_touch_timestamp as string)),coalesce((select value.int_value from unnest(event_params) where key = 'ga_session_id'),user_first_touch_timestamp)) as unique_session_id,

  timestamp_micros(event_timestamp) as event_timestamp, event_name, device.category as device,

  -- making a clean page_location without parameters etc
  -- beginning with regexp_replace to remove the final / from the string
  lower(REGEXP_REPLACE(
  -- if the page location has a ?
  if(regexp_contains((SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_location'),r'\?'),
  -- then return the string until the ?, minus 1.
  left((SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_location'),
  regexp_instr((SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_location'), r'\?')-1),
  -- else provide the string
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_location'))
  -- and here is the end of the regexp_replace to replace the final / with nothing, as well as https:// and www. with nothing
  , r'(https?://(?:www\.)?|\/$)','')) as page_location_clean,

  -- signal if the entire session was engaged based on the below
  MAX(
    (case
      when (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'session_engaged') = '1'
      then 1
      when (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'session_engaged') = 1
      then 1
      when (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'engaged_session_event') = 1
      then 1
      else 0 end
      )
    )
  OVER (
    PARTITION BY concat(coalesce(user_pseudo_id,cast(user_first_touch_timestamp as string)),coalesce((select value.int_value from unnest(event_params) where key = 'ga_session_id'),user_first_touch_timestamp))
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING -- this ensures all rows in the partition are assessed
  ) as engaged_session,

from `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_202101*` --only Jan 2021

where event_name = 'page_view'

)

order by 1, 2
"""

project_id = "dummy-name-bq" ##adjust accordingly


df = read_gbq(query, project_id=project_id)

df.to_csv('./data/output/GA4 sample - BQ public data.csv', index=False)
