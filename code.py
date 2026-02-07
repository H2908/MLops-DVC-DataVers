import pandas as pd
import os
data={'Name':['Alice','Bob','Charlie'],'Age':[25,30,35],'City':['New York','Los Angeles','Chicago']}
df=pd.DataFrame(data)
## Adding new row to df for v2
#new_row_loc={'Name':'David','Age':40,'City':'Houston'}
#df.iloc[len(df.index)]=new_row_loc

## Adding new row to df for v3
#new_row_loc2={'Name':'David','Age':40,'City':'Houston'}
#df.loc[len(df.index)]=new_row_loc2

# Ensure the 'data' directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# define the file path
file_path = os.path.join(data_dir, 'data.csv')
# Save the DataFrame to a CSV file
df.to_csv(file_path, index=False)
print(f"DataFrame saved to {file_path}")