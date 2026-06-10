# SMS Spam Detector 🚀

ML model that detects spam SMS with 97.94% accuracy.

## Day 3 Results
- **Dataset:** 5572 real SMS from Kaggle
- **Model:** Naive Bayes + NLP
- **Accuracy:** 97.94% on 1115 test messages
- **Tech Stack:** Python, Pandas, Scikit-learn

## Test Cases
1. "Congratulations! You won a free iPhone" -> SPAM ✅
2. "Hi mom, will reach home by 8pm" -> HAM ✅

## How to Run
```bash
pip install pandas matplotlib seaborn scikit-learn
python fraud_detector.py
