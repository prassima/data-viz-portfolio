For the data scripts, I utilised the following approach:
- Installed miniconda https://docs.anaconda.com/miniconda/install/#quick-command-line-install
- Then, to get the appropriate packages and libraries, run the following in terminal, with current directory as the base of this repo (which is for the requirements.txt file):
- `conda create -n myenv`
- `conda activate myenv`
- `conda install pip`
- `pip install -r requirements.txt`