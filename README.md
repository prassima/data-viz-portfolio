<h1>My Portfolio Site</h1>

<h2>Description</h2>
<p>This repo contains the the HTML, CSS and JS code for the GitHub pages site linked to this project. It also contains the Python scripts that I created to Extract and Transform the data which is visualised on the Samples page. These scripts produce the data in csv outputs.</p>

<h3>To set up the Python environment locally to run the data scripts yourself:</h3>
<ul>
<li>Download the .py files contained within the <code>/data/scripts/</code> directory, as well as the <code>requirements.txt</code> file</li>
<li>Ensure you have python installed locally. For ease, I recommend using <a href= https://docs.anaconda.com/miniconda/install/#quick-command-line-install>miniconda</a></li>
<li>Create virtual environment and install appropriate packages and libraries. To do this, run the following in terminal, with current directory set to where you have downloaded the .py and requirements.txt files:</li>
  <ul>
  <li><code>conda create -n myenv</code> (I have used a generic name, myenv, but feel free to adjust)</li>
  <li><code>conda activate myenv</code></li>
  <li><code>conda install pip</code> (necessary if using miniconda)</li>
  <li><code>cd '/directory/to/where/scripts/are'</code></li>
  <li><code>pip install -r requirements.txt</code></li>
  </ul>
</ul>
<p>You will then be able to execute these python files in your code editor of choice</p>
