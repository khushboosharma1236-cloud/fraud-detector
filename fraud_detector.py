# FRAUD DETECTOR - DAY 1 + 2 + 3 COMPLETE
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# ========== DAY 1: DATA LOAD ==========
print("--- Loading Data ---")
df = pd.read_csv('spam.csv', encoding='latin-1')
df = df.iloc[:, :2]  # Pehle 2 columns le lo
df.columns = ['label', 'message']

print(f"Dataset loaded: {df.shape[0]} SMS")
print("\nFirst 5 messages:")
print(df.head())

# ========== DAY 2: DATA ANALYSIS + GRAPH ==========
print("\n--- Making Graph ---")
plt.figure(figsize=(6,4))
sns.countplot(x='label', data=df, hue='label', palette=['green','red'], legend=False)
plt.title('Spam vs Ham SMS Count')
plt.xlabel('Type')
plt.ylabel('Count')
plt.savefig('spam_vs_ham.png') # Graph save kar dega
plt.show()

# ========== DAY 3: ML MODEL ==========
print("\n--- ML Model Training ---")

# 1. TEXT CLEANING FUNCTION
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# 2. SAARI SMS CLEAN KARO
print("Cleaning 5572 SMS...")
df['clean_message'] = df['message'].apply(clean_text)
print("Cleaning done!")

# 3. TEXT KO NUMBERS ME BADLO
vectorizer = CountVectorizer(stop_words='english', max_features=3000)
X = vectorizer.fit_transform(df['clean_message'])
y = df['label']
print("Text converted to numbers. Shape:", X.shape)

# 4. TRAIN-TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Train size:", X_train.shape[0], "Test size:", X_test.shape[0])

# 5. NAIVE BAYES MODEL TRAIN KARO
model = MultinomialNB()
model.fit(X_train, y_train)
print("Model trained!")

# 6. ACCURACY CHECK KARO
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# 7. APNA SMS TEST KARO
def predict_sms(sms):
    cleaned = clean_text(sms)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    return prediction

# TEST CASES
print("\n--- Testing Custom SMS ---")
test1 = "Congratulations! You won a free iPhone. Click here now"
test2 = "Hi mom, will reach home by 8pm"
print("Test 1:", test1, "->", predict_sms(test1))
print("Test 2:", test2, "->", predict_sms(test2))
print("\n--- Day 3 Complete ---")