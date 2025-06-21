import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,accuracy_score

df = pd.read_csv("C:/Users/athin/OneDrive/Desktop/AI projects/train.csv")
df['Sex'] = df['Sex'].map({'male':0,'female':1})
df['Embarked'] = df['Embarked'].map({'C':1,'Q':0,'S':2})
df['Age'] = df['Age'].fillna(df['Age'].mean())
df = df.dropna()

x = df.drop(['Survived','Name','Ticket','Cabin'], axis=1)
y = df['Survived']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

value = pd.DataFrame([{
    'PassengerId': int(input('Enter Passenger ID: ')),
    'Pclass': int(input('Enter Passenger Class (1, 2, or 3): ')),
    'Sex': int(input('Enter gender (0 for male and 1 for female): ')),
    'Age': float(input('Enter Age: ')),
    'SibSp': int(input('Enter number of siblings/spouses aboard: ')),
    'Parch': int(input('Enter number of parents/children aboard: ')),
    'Fare': float(input('Enter Fare: ')),
    'Embarked': int(input('Enter Embarked_C (1),Embarked_Q (0),Embarked_S (2): '))
}])

predicted_survival = model.predict(value)
print(f"Predicted Survival: {'Survived' if predicted_survival[0] == 1 else 'Did not survive'}")