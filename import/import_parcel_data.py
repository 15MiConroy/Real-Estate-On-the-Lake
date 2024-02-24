import pandas as pd
import polars as pl
import time



# read in from csv to pandas dataframe
df = pd.read_csv('C:/Users/Micha/OneDrive/Documents/PARCELS_LAK_OH_JAN_2024.csv')
# df = pl.read_csv('C:/Users/Micha/OneDrive/Documents/PARCELS_LAK_OH_JAN_2024.csv')

# Print the head of the DataFrame
print(df.head())