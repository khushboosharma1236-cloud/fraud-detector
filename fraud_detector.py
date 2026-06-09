import pandas as pd

df = pd.read_csv('spam.csv', encoding='latin-1')
df = df.iloc[:,:2]
df.columns = ['label', 'message']
print("Dataset loaded! Total SMS:", len(df))
print("\nFirst 5 messages:")
print(df.head())