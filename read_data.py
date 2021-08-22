import numpy as np
import pandas as pd

def read_data():
    data = pd.read_csv("ratings.csv")
    # print(data.head())
    return data
