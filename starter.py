import subprocess
import sys
from sklearn.datasets import load_breast_cancer, load_diabetes
from sklearn.model_selection import train_test_split


# import necessary libraries and load the dataset
from sklearn.linear_model import LinearRegression


from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from explainerdashboard import RegressionExplainer, ClassifierExplainer, ExplainerDashboard, ExplainerHub
import pandas as pd

import streamlit as st
from streamlit.components.v1 import iframe

if __name__ == "__main__":
    subprocess.run(["python", "explainer-dashboard.py", "&"]) 
    subprocess.run(["streamlit", "run", "main.py", "&"]) 
