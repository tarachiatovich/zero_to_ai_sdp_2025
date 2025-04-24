# Import all of our imports to make sure they're all present
import os
import sys
import matplotlib.pyplot
import numpy
import pandas
import seaborn
import xgboost
import sklearn
import skforecast
import ucimlrepo 
import statsmodels

def test_python_version():
    assert sys.version_info[:2] == (3, 11), "Python version must be exactly 3.11"
