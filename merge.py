import pandas as pd
import os

appended_data = []
files = os.listdir('excel')
for file in files:
    df = pd.read_excel('excel/{}'.format(file))
    appended_data.append(df)

appended_data = pd.concat(appended_data)
# write DataFrame to an excel sheet
appended_data.to_excel('appended.xlsx',index=False)