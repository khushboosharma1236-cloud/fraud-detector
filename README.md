# SMS Fraud Detector by Khushboo Sharma 🚀

[![Live App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://khushboo-fraud-detector.streamlit.app)

A Machine Learning project to detect Fraud/Spam SMS with **97.94% accuracy**. Built from scratch and deployed live on Streamlit Cloud.

### 🔴 Live Demo
**Try the app here:** https://khushboo-fraud-detector.streamlit.app

---

## 📖 My Journey: Day 1 to Deployment

### **Day 1: Problem & Dataset**
Started with the problem of rising SMS scams in India. Found the `SMS Spam Collection` dataset with 5,574 real SMS messages.

### **Day 2: Data Cleaning & EDA**
- Cleaned the dataset using Pandas
- Handled missing values and duplicates
- Did Exploratory Data Analysis to understand spam vs ham patterns
- Visualized data using Matplotlib & Seaborn

### **Day 3: NLP Preprocessing**
- Used NLP techniques to process text
- Applied CountVectorizer to convert SMS text into numerical vectors
- Prepared data for ML model training

### **Day 4: Model Training & Evaluation**
- Trained a **Multinomial Naive Bayes** model using Scikit-learn
- Achieved **97.94% accuracy** on test data
- Tested with Confusion Matrix & Classification Report
- Model successfully detects lottery scams, fake KYC, phishing links

### **Day 5: Deployment Challenge**
- Built web app using **Streamlit**
- Faced `ModuleNotFoundError: streamlit` during deployment
- Fixed it by adding `requirements.txt` with all dependencies
- Debugged model bug where it only predicted "Safe"
- Finally deployed successfully on Streamlit Cloud

---

## 🎯 Features
- Detects fraud types: Lottery scam, Bank KYC fraud, Phishing links
- Real-time SMS prediction
- 97.94% Accuracy on test dataset
- Clean & simple UI

## 🛠️ Tech Stack
- **Language:** Python
- **ML Library:** Scikit-learn
- **Data:** Pandas, Numpy  
- **NLP:** CountVectorizer
- **Visualization:** Matplotlib, Seaborn
- **Deployment:** Streamlit Cloud
- **Version Control:** Git & GitHub

## 📊 Test Cases
**Fraud SMS:** `CONGRATULATIONS! You won Rs 5,00,000. Call 9876543210`  
**Result:** ❌ FRAUD ALERT: Ye SPAM hai! Block kar do.

**Safe SMS:** `Hi mummy, main theek hu. Office pahunch gayi.`  
**Result:** ✅ Safe hai

## 🚀 How to Run Locally
1. Clone repo: `git clone https://github.com/khushboosharma1236-cloud/fraud-detector.git`
2. Install: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`

---
## 💡 What I Learned
This project taught me the complete ML lifecycle: from data cleaning, EDA, NLP, model training, to final cloud deployment. Debugging deployment errors was the toughest but most rewarding part.

**Built with ❤️ by Khushboo Sharma**  
**For Amazon ML Summer School 2026**
