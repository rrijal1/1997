import pandas as pd
import pyplot as plt

def load_parquet_data(file):
    '''
    Returns parquet file as pandas dataframe
    input: parquet file
    output: pandas dataframe
    '''
    return pd.read_parquet(file)

df = load_parquet_data("input/content.parquet")

