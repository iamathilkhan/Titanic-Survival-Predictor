# 🚢 Titanic Survival Predictor

<p align="center">
  <strong>A machine learning classification model that predicts passenger survival on the Titanic using Logistic Regression</strong>
  <br><br>
  <a href="#overview">Overview</a> •
  <a href="#features">Features</a> •
  <a href="#technology-stack">Technology</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#model-evaluation">Evaluation</a>
</p>

---

## 📋 Overview

**Titanic Survival Predictor** is a machine learning classification project that leverages **Logistic Regression** to predict whether a passenger survived the Titanic disaster. This project demonstrates practical implementation of supervised learning for binary classification on the famous Titanic dataset.

### Project Goal
Predict survival (Yes/No) of passengers aboard the Titanic based on demographic and travel information.

### Dataset
- **Source**: [Titanic dataset from Kaggle](https://www.kaggle.com/c/titanic/data)
- **Total Records**: 891 passengers
- **Target Variable**: Survival (1 = Survived, 0 = Did Not Survive)

### Use Cases
- 📊 **Historical Data Analysis** - Understand survival patterns
- 🎓 **Educational ML Project** - Learn classification techniques
- 💼 **Business Intelligence** - Demographic risk assessment
- 🔍 **Data Science Portfolio** - Showcase ML fundamentals

---

## ✨ Key Features

- 🤖 **Logistic Regression Model** - Industry-standard classification algorithm
- 📊 **Comprehensive Feature Engineering** - Demographic and travel data analysis
- 🎯 **Binary Classification** - Clear survive/not survive prediction
- 📈 **Data Preprocessing** - Handling missing values and encoding
- 💾 **Model Persistence** - Trained model ready for inference
- 📉 **Performance Metrics** - Accuracy evaluation with detailed analysis
- 🔧 **Easy Setup** - Simple installation and execution

---

## 🧠 Features Used for Prediction

| Feature | Description | Data Type |
|---------|-------------|-----------|
| **Pclass** | Passenger Class (1st, 2nd, 3rd) | Categorical |
| **Sex** | Gender (Male = 0, Female = 1) | Categorical (Encoded) |
| **Age** | Age of passenger (Mean imputation) | Numerical |
| **SibSp** | Number of siblings/spouses aboard | Numerical |
| **Parch** | Number of parents/children aboard | Numerical |
| **Fare** | Ticket fare paid | Numerical |
| **Embarked** | Port of Embarkation (C=1, Q=0, S=2) | Categorical (Encoded) |

---

## 🛠️ Technology Stack

![Python](https://img.shields.io/badge/-Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/-Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/-NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/-Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/iamathilkhan/Titanic-Survival-Predictor.git
cd Titanic-Survival-Predictor
```

### Step 2: Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install pandas scikit-learn numpy matplotlib seaborn
```

### Step 4: Download Dataset
1. Download the Titanic dataset from [Kaggle](https://www.kaggle.com/c/titanic/data)
2. Place `train.csv` in the project root directory
3. Verify the path in your script

---

## 📖 Usage

### Running the Model

1. **Execute the script:**
   ```bash
   python logistic_model.py
   ```

2. **Expected Output:**
   ```
   Model Training Started...
   Data preprocessing completed
   Model training finished
   Accuracy Score: 0.82 (82%)
   Predictions generated successfully
   ```

3. **Make Predictions:**
   ```python
   # Example: Predict survival for a new passenger
   # Passenger: Female, 25 years old, 1st class, $100 fare
   new_passenger = [[1, 1, 25, 0, 0, 100, 1]]
   prediction = model.predict(new_passenger)
   # Output: 1 (Survived) or 0 (Did Not Survive)
   ```

### Example Predictions

| Pclass | Sex | Age | SibSp | Parch | Fare | Embarked | Prediction |
|--------|-----|-----|-------|-------|------|----------|------------|
| 1 | F (1) | 25 | 0 | 0 | $100 | S (2) | ✅ Survived |
| 3 | M (0) | 30 | 1 | 0 | $15 | S (2) | ❌ Did Not Survive |
| 1 | M (0) | 40 | 1 | 1 | $250 | C (1) | ❓ Uncertain |

---

## 📁 Project Structure

```
Titanic-Survival-Predictor/
├── logistic_model.py          # Main model script
├── data_preprocessing.py       # Data cleaning & feature engineering
├── train.csv                   # Titanic dataset
├── requirements.txt            # Python dependencies
├── models/
│   └── titanic_model.pkl       # Trained model
├── notebooks/
│   └── analysis.ipynb          # Exploratory data analysis
└── README.md
```

---

## 🔄 Algorithm Overview

**Logistic Regression Process:**

```
Raw Data (Train.csv)
  ↓
Data Cleaning & Preprocessing
  ↓
Feature Engineering & Encoding
  ↓
Train/Test Split (80/20)
  ↓
Logistic Regression Training
  ↓
Model Evaluation & Metrics
  ↓
Survival Predictions
```

### Data Preprocessing Steps
1. **Handle Missing Values** - Fill Age with mean, Embarked with mode
2. **Feature Encoding** - Convert categorical variables to numerical
3. **Feature Scaling** - Normalize features for better performance
4. **Train/Test Split** - 80% training, 20% testing

---

## 📊 Model Configuration

| Parameter | Value |
|-----------|-------|
| **Algorithm** | Logistic Regression |
| **Solver** | liblinear |
| **Max Iterations** | 1000 |
| **Train/Test Split** | 80/20 |
| **Feature Scaling** | StandardScaler |

---

## 📈 Model Evaluation

### Performance Metrics

| Metric | Value | Interpretation |
|--------|-------|-----------------|
| **Accuracy Score** | ~82% | Overall prediction correctness |
| **Precision** | ~79% | True positive among predicted positives |
| **Recall** | ~73% | True positive detection rate |
| **F1-Score** | ~0.76 | Balanced precision-recall metric |

### Results Interpretation
- ✅ **High Accuracy** - Model correctly predicts survival in 82% of cases
- 📊 **Balanced Performance** - Good precision and recall balance
- 🎯 **Classification Power** - Reliable for survival prediction

---

## 🔍 Exploratory Data Analysis

### Key Insights
- **Gender Impact** - Females had higher survival rate (~74%)
- **Class Effect** - 1st class passengers had better survival odds
- **Age Factor** - Children had higher survival probability
- **Fare Correlation** - Higher ticket prices correlate with survival

---

## 🔧 Customization

### Adjust Model Parameters
```python
from sklearn.linear_model import LogisticRegression

# Modify parameters
model = LogisticRegression(
    max_iter=1000,        # Increase iterations
    solver='lbfgs',       # Try different solver
    random_state=42
)
```

### Add More Features
- Cabin information
- Ticket number patterns
- Passenger name prefixes
- Family survival history

---

## 🚨 Troubleshooting

| Issue | Solution |
|-------|----------|
| **FileNotFoundError: train.csv** | Ensure CSV is in project root directory |
| **ModuleNotFoundError** | Run `pip install -r requirements.txt` |
| **Poor accuracy** | Try feature engineering or parameter tuning |
| **Memory issues** | Use data sampling or chunking for large datasets |

---

## 📚 Learning Resources

- [Logistic Regression - Scikit-learn](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)
- [Titanic Dataset Analysis](https://www.kaggle.com/c/titanic)
- [Binary Classification Guide](https://developers.google.com/machine-learning/crash-course/classification)
- [Pandas Data Manipulation](https://pandas.pydata.org/docs/)

---

## 📝 License

This project is open source and available under the **MIT License**.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📬 Support & Contact

- **Email:** athilkhan2005@gmail.com
- **LinkedIn:** [Connect here](https://linkedin.com/in/ahamed-athil-khan)
- **GitHub Issues:** [Report issues](https://github.com/iamathilkhan/Titanic-Survival-Predictor/issues)

---

## 🙏 Acknowledgments

- Titanic dataset from Kaggle
- Scikit-learn for ML libraries
- Data preprocessing techniques from industry best practices
- Contributors and feedback providers

---

<p align="center">
  <b>⭐ If you found this project helpful, please give it a star! ⭐</b>
  <br>
  <sub>Made with ❤️ by Ahamed Athil Khan | Last Updated: November 2025</sub>
</p>

---

## 📋 Quick Reference

```bash
# Clone
git clone https://github.com/iamathilkhan/Titanic-Survival-Predictor.git

# Install
pip install -r requirements.txt

# Run
python logistic_model.py

# Dataset
Download from: https://www.kaggle.com/c/titanic/data
Place train.csv in project root
```
