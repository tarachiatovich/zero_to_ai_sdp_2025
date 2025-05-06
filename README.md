# zero_to_ai_sdp_2025
Worked examples for Zero to AI presentation at 2025 SDP Convening

# Installing Miniconda
We will be using conda for package management and environment setup. Please show up with Miniconda installed on your computer. You can do so by:
- Going to [this page](https://www.anaconda.com/download).
- Clicking under the green Submit button (if you do not wish to provide your email --> they make it hard to see the skip registration option!).
- Navigating down to the Miniconda Installers on that page.
- Selecting the proper Graphical Installer for your computer (Mac or Windows) and when prompted, select the option to install for "just me".

# Installing Git

We recommend installing Git, though we will provide you with a work-around if you would prefer to skip this step. Instructions are on [this page](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Simply look for the directions for your computer.

# Environment Setup
## Option 1: Use a virtual environment (recommended)

If you are comfortable using the terminal (on a Mac) or the prompt (on Windows) and are familiar with Git, we recommed using a virtual environment. The steps are outlined below according to your operating system. 

Start by cloning this repository and then follow the proper directions below for your operating system.

For Mac:
1. In the terminal, navigate to the folder for this Git repository.
2. Run the following command in the terminal:
```sh create_env_and_download.sh```

For Windows:
1. Open Anaconda Prompt (use the search bar if needed to locate it).
2. Navigate to the folder for this Git repository.
3. Run the following three lines of code in the prompt:
```
conda env create -f environment.yml
conda activate zero_to_ai_environment

pytest
```

Finally we will require a couple of commands to be run to get some of the data we need for the AI applications. If you would like to run the emebdding notebook you will need to run the following line of code:

```python -m spacy download en_core_web_lg```

The works the same whether you are on a Mac running the code above in the terminal or on a Windows computer running it in the Anaconda Prompt.

## Option 2: Install packages globally

If you are a new or infrequent Python user and have difficulty following the steps outlined above to use a virtual environment, you can opt to install the packages globally. (Read more [here](https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c/) about why virtual environments are worth the effort if you will be using Python regularly.)

To install packages globally, use the steps below, which work for both a Mac and Windows computer:

1. Clone this Git repository or, if you prefer, download the contents of this repository by clicking the down arrow on the green "Code" button on the repository's home page and selecting "Download ZIP".
2. Open Anaconda Navigator on your computer, find Jupyter Notebook, and click Launch.
3. Navigate to the folder with the downloaded contents of this repository, and open the file named `pip_install.ipynb`.
4. Run each cell using the Shift + Enter keyboard shortcut.

You should now be set to work with the notebooks that have our worked examples!