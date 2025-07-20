import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('startup_funding.csv')
df = pd.read_csv('C:\INDIAN_STARTUP_EDA_STREAMLIT\startup_funding.csv')
# checking if our dataset is loading or not
# st.dataframe(df)
print(df.head())
# print(df['Startup Name'].to_list())