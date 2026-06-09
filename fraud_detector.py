import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# DAY 1: Load data + Fix column names
df = pd.read_csv('spam.csv', encoding='latin-1')

# Sirf pehle 2 column lo aur naam badlo
df = df.iloc[:, :2]
df.columns = ['label', 'message']

print("Total SMS Loaded:", len(df))

# DAY 2: Data Analysis
print("\n--- DAY 2: Data Analysis ---")

print("\nSpam vs Ham Count:")
print(df['label'].value_counts())

print("\nNull Values Check:")
print(df.isnull().sum())

print("\nFirst 5 Messages:")
print(df.head())

# DAY 2: Graph banao
print("\n--- Making Graph ---")
plt.figure(figsize=(6,4))
sns.countplot(x='label', data=df, palette=['green','red'])
plt.title('Spam vs Ham SMS Count')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()