# 🚢 Titanic Survival Predictor - Logistic Regression

This project uses the Titanic dataset to build a **logistic regression model** that predicts whether a passenger survived the Titanic disaster based on various features such as age, gender, passenger class, and fare.

---

## 🔍 Project Overview

- **Goal**: Predict survival (Yes/No) of passengers aboard the Titanic.
- **Algorithm**: Logistic Regression
- **Dataset**: [Titanic dataset from Kaggle](https://www.kaggle.com/c/titanic/data)

---

## 🧠 Features Used

- `Pclass`: Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)
- `Sex`: Gender (encoded: male = 0, female = 1)
- `Age`: Age of the passenger (missing values filled with mean)
- `SibSp`: Number of siblings/spouses aboard
- `Parch`: Number of parents/children aboard
- `Fare`: Ticket fare
- `Embarked`: Port of Embarkation (encoded: C = 1, Q = 0, S = 2)

---

## 🛠 Technologies Used

- Python
- Pandas
- Scikit-learn

---

## 🧪 Model Evaluation

- **Accuracy Score**: ~82%
- **R² Score**: ~-0.08 (Note: R² isn't ideal for classification)

---

## 📥 How to Use

1. Clone the repo or download the `.py` file.
2. Make sure you have the Titanic dataset (`train.csv`) in the correct path.
3. Run the script:
   ```bash
   python logistic_model.py
