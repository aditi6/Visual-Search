import pandas as pd
import random
import numpy as np

# Read Exp1A data
df = pd.read_csv('Experiment1A.csv')

# view the first few rows of the dataframe
print(df.head())

# Create a new dataframe with columns loc1 to loc 36
df_locs = df.loc[:, 'loc1':'loc36']


# Iterate through the columns

columns=['loc1','loc2','loc3','loc4','loc5','loc6','loc7','loc8','loc9','loc10','loc11','loc12','loc13','loc14','loc15','loc16','loc17','loc18','loc19','loc20','loc21','loc22','loc23','loc24','loc25','loc26','loc27','loc28','loc29','loc30','loc31','loc32','loc33','loc34','loc35','loc36']

for col in  columns:
    # If target ID is 0 and the value in the loc column is 1, change the value to 1
    df_locs[col] = np.where((df['Target ID'] == 0) & (df_locs[col] == 1), 1, df_locs[col])

    # If distractor colours is 3 and the value in the loc column is 3, change the value to either 4 or 5 with 50:50 probability. Iterate through the rows
    for i, row in df_locs.iterrows():
        x=random.randint(0,1)
        if df['distractorColors'][i] == 3:
            for j in range(36):
                if df_locs.iloc[i, j] == 3:
                    df_locs.iloc[i, j] = 5 if x<=0.5 else 6

    # If distractor colours is 1 and the value in the loc column is 2, change the value to 3
    df_locs[col] = np.where((df['distractorColors'] == 1) & (df_locs[col] == 2), 3, df_locs[col])

    # If distractor colours is 2 and the value in the loc column is 2, change the value to 4
    df_locs[col] = np.where((df['distractorColors'] == 2) & (df_locs[col] == 2), 4, df_locs[col])


    # If target ID is 1 and the value in the loc column is 1, change the value to 2
    df_locs[col] = np.where((df['Target ID'] == 1) & (df_locs[col] == 1), 2, df_locs[col])




    
#Append subject and trial columns to df_locs
df_locs['Subject'] = df['Subject']
df_locs['Trial'] = df['Trial']

# Display df_locs
print(df_locs.head())

# save dataframe as locations.csv
df_locs.to_csv('locations.csv', index=False)




