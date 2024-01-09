import numpy as np
import pandas as pd
data_united = pd.read_csv("/Users/anishyadlapalli/FlightPredictions/United_Airlines_Statistics_Departures.csv")
data_delta = pd.read_csv("/Users/anishyadlapalli/FlightPredictions/Delta_AirlinesDetailed_Statistics_Departures.csv")
data_southwest = pd.read_csv("/Users/anishyadlapalli/FlightPredictions/SouthWest_Detailed_Statistics_Departures.csv")

# Create a list of dataframes file names
df_files = [data_united, data_delta, data_southwest]

print(data_delta.columns)
# Merge the dataframes by the date column using an outer join
merged_df = pd.merge(df_files[0], df_files[1], on="Date (MM/DD/YYYY)", how="right")
print(merged_df) # print the first set of them.
print(merged_df.columns) # let's see the columns that they have.  
merged_df = pd.merge(merged_df, df_files[2], on="Date (MM/DD/YYYY)", how="right")
print(merged_df)

merged_df.to_csv('data.csv')