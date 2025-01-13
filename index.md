<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flourish Grid</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        .grid-container {
            display: grid;
            grid-template-columns: repeat(2, 1fr); /* 2 columns */
            gap: 20px;
            max-width: 1200px;
            margin: auto;
        }

        .grid-item {
            background: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 8px;
            overflow: hidden;
            padding: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .flourish-embed {
            width: 100%;
            height: 300px; /* Adjust height to fit visuals */
        }

        @media (max-width: 768px) {
            .grid-container {
                grid-template-columns: 1fr; /* Stack items on smaller screens */
            }
        }
    </style>
</head>
<body>

<h1>Hi, I am Paris.</h1>
<p>
    I bring datasets to life through Business Intelligence, data visualisation, data storytelling, and staff upskilling. Together, we embed that data into strategic decision-making.
</p>
<p>
    With over 10 years of experience across a range of industries from FMCG to Non-profit, I have a proven track record in delivering data-driven solutions that drive growth and optimisation.
</p>
<p>
    I care deeply about people, and know that the insights we attain from data are only useful if the right people understand what to do about them.
</p>

<div class="grid-container">
    <div class="grid-item">
        <div class="flourish-embed flourish-chart" data-src="visualisation/21093185">
            <script src="https://public.flourish.studio/resources/embed.js"></script>
            <noscript>
                <img src="https://public.flourish.studio/visualisation/21093185/thumbnail" width="100%" alt="chart visualization" />
            </noscript>
        </div>
    </div>

    <div class="grid-item">
        <div class="flourish-embed flourish-scatter" data-src="visualisation/21093566">
            <script src="https://public.flourish.studio/resources/embed.js"></script>
            <noscript>
                <img src="https://public.flourish.studio/visualisation/21093566/thumbnail" width="100%" alt="scatter visualization" />
            </noscript>
        </div>
    </div>

    <div class="grid-item">
        <div class="flourish-embed flourish-chart" data-src="visualisation/21111518">
            <script src="https://public.flourish.studio/resources/embed.js"></script>
            <noscript>
                <img src="https://public.flourish.studio/visualisation/21111518/thumbnail" width="100%" alt="chart visualization" />
            </noscript>
        </div>
    </div>

    <div class="grid-item">
        <div class="flourish-embed flourish-scatter" data-src="visualisation/21114719">
            <script src="https://public.flourish.studio/resources/embed.js"></script>
            <noscript>
                <img src="https://public.flourish.studio/visualisation/21114719/thumbnail" width="100%" alt="scatter visualization" />
            </noscript>
        </div>
    </div>

    <div class="grid-item">
        <div class="flourish-embed flourish-chart" data-src="visualisation/21114125">
            <script src="https://public.flourish.studio/resources/embed.js"></script>
            <noscript>
                <img src="https://public.flourish.studio/visualisation/21114125/thumbnail" width="100%" alt="chart visualization" />
            </noscript>
        </div>
    </div>
</div>

</body>
</html>
