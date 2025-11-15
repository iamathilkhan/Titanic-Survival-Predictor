from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('titanic_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    passenger_id = int(request.form['passenger_id'])
    pclass = int(request.form['pclass'])
    sex = int(request.form['sex'])
    age = float(request.form['age'])
    sibsp = int(request.form['sibsp'])
    parch = int(request.form['parch'])
    fare = float(request.form['fare'])
    embarked = int(request.form['embarked'])

    # Create DataFrame for prediction
    value = pd.DataFrame([{
        'PassengerId': passenger_id,
        'Pclass': pclass,
        'Sex': sex,
        'Age': age,
        'SibSp': sibsp,
        'Parch': parch,
        'Fare': fare,
        'Embarked': embarked
    }])

    # Make prediction
    predicted_survival = model.predict(value)
    result = 'Survived' if predicted_survival[0] == 1 else 'Did not survive'

    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
