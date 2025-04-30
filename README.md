# zero_to_ai_sdp_2025
Worked examples for Zero to AI presentation at 2025 SDP Convening

# Environment Setup
We will be using conda for package management and environment setup. Please show up with Miniconda installed on your computer. You can do so by going to [this page](https://www.anaconda.com/download), clicking under the green Submit button (if you do not wish to provide your email), and then navigating down to the Miniconda Installers on that page. From there, select the proper Graphical Installer for your computer (Mac or Windows).

To configure your python environment properly, please run the following command based on your Mac/Windows status:

For Mac you can simply run the following line of code in the terminal
```sh create_env_and_download.sh```

For Windows open Anaconda Prompt and run the following three lines of code
```
conda env create -f environment.yml
conda activate zero_to_ai_environment

pytest
```

Finally we wil require a couple of commands to be run to get some of the data we need for the AI applications. If you would like to run the emebdding ntoebook you will need to run 

```python -m spacy download en_core_web_lg```


# Installing Git

We also recommend installing Git. Instructions are on [this page](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Simply look for the directions for your computer.