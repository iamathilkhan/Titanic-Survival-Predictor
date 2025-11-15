import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, accuracy_score
import joblib

# Load and preprocess data
df = pd.read_csv("train.csv")
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df['Embarked'] = df['Embarked'].map({'C': 1, 'Q': 0, 'S': 2})
df['Age'] = df['Age'].fillna(df['Age'].mean())
df = df.dropna()

x = df.drop(['Survived', 'Name', 'Ticket', 'Cabin'], axis=1)
y = df['Survived']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Save the trained model
joblib.dump(model, 'titanic_model.pkl')
print("Model saved as titanic_model.pkl")
