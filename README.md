# IDS706-python-template
### by Titus Robin

**Summary**

The purpose of this project is using Polars to load a dataframe. I used a pl.DataFrame as a sample data and test its descriptions using the function polars_descriptive_stats_*(). The visualization on a scatter plot.

# Dataset 
The [dataset](https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv) is about about various cars Models, Miles per gallon, Cylinders, Gear etc...

# Functions 
The Polars DataFrame is passed into the functions which return:
- Mean

# Visualisation
A scatter plot is generated to compare the variables of Miles per Gallon and Horsepower
<img width="712" alt="Screen Shot 2023-09-12 at 9 51 11 PM" src="https://github.com/nogibjj/week2_tra29/assets/143838819/ca88f222-4159-4f8e-bb82-3d3729aae623">

Automation
used takes into Consideration

1. devcontainer
The .devcontainer folder mainly contains two files -

Dockerfile defines the environment variables - essentially it ensures that all collaborators using the repository are working on the same environment to avoid conflicts and version mismatch issues devcontainer.json is a json file that specifies the environment variables including the installed extensions in the virtual environment

2. Makefile
The Makefile contains instructions for installing packages (specified in requirements.txt), formatting the code (using black formatting), testing the code (running all the sample python code files starting with the term 'Check...' ), and linting the code using pylint

3. GitHub Actions
Github Actions uses the main.yml file to call the functions defined in the Makefile based on triggers such as push or pull. Currently, every time a change is pushed onto the repository, it runs the install packages, formatting the code, linting the code, and then testing the code functions

4. Requirements.txt
The requirements.txt file has a list of packages to be installed for any required project. Currently, my requirements file only contains generic python packages, more specific packages can and will be added depending on scope of projects over time.
