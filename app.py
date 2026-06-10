# DAY 4: STREAMLIT WEB APP
import streamlit as st
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. MODEL TRAIN KARO - Background me
@st.cache_resource
def load_model():
    df = pd.read_csv('spam.csv', encoding='latin-1')
    df = df.iloc[:, :2]
    df.columns = ['label', 'message']

    def clean_text(text):
        text = text.lower()
        text = re.sub(r'[^a-z\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    df['clean_message'] = df['message'].apply(clean_text)
    vectorizer = CountVectorizer(stop_words='english', max_features=3000)
    X = vectorizer.fit_transform(df['clean_message'])
    y = df['label']

    model = MultinomialNB()
    model.fit(X, y)
    return model, vectorizer, clean_text

model, vectorizer, clean_text = load_model()

# 2. WEBSITE KA UI
st.title('📱 Fraud Detector by Khushboo')
st.subheader('SMS Spam Checker - 97.94% Accurate')

st.write('Neeche SMS paste karo aur check karo ki Fraud hai ya nahi')

# 3. USER INPUT BOX
user_sms = st.text_area('Apna SMS yahan likho:', height=150)

# 4. PREDICT BUTTON
if st.button('Check Karo'):
    if user_sms:
        cleaned = clean_text(user_sms)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]

        if prediction == 'spam':
            st.error('🚨 FRAUD ALERT: Ye SPAM hai! Block kar do.')
        else:
            st.success('✅ SAFE: Ye HAM hai. Tension nahi lene ka.')
    else:
        st.warning('Pehle SMS to likho yaar 😅')

st.write('---')
st.write('Made with ❤️ using Python + ML | Accuracy: 97.94%')