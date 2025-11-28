from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model
model = joblib.load('titanic_model.pkl')

@app.route('/')
def home():
    return jsonify({'message': 'Titanic Survival Predictor API'})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data
        data = request.get_json()

        # Extract features
        passenger_id = int(data['passenger_id'])
        pclass = int(data['pclass'])
        sex = int(data['sex'])
        age = float(data['age'])
        sibsp = int(data['sibsp'])
        parch = int(data['parch'])
        fare = float(data['fare'])
        embarked = int(data['embarked'])

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

        return jsonify({'prediction': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
