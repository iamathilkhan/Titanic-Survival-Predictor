import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    passenger_id: '',
    pclass: '',
    sex: '',
    age: '',
    sibsp: '',
    parch: '',
    fare: '',
    embarked: ''
  });
  const [prediction, setPrediction] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:5000/predict', formData);
      setPrediction(response.data.prediction);
    } catch (error) {
      console.error('Error making prediction:', error);
      setPrediction('Error: Unable to make prediction');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <div className="container">
        <header className="header">
          <h1>Titanic Survival Predictor</h1>
          <p className="subtitle">Predict passenger survival based on historical data</p>
        </header>

        <div className="form-container">
          <form onSubmit={handleSubmit} className="prediction-form">
            <div className="form-grid">
              <div className="form-group">
                <label htmlFor="passenger_id">Passenger ID</label>
                <input
                  type="number"
                  id="passenger_id"
                  name="passenger_id"
                  value={formData.passenger_id}
                  onChange={handleChange}
                  placeholder="Enter passenger ID"
                  required
                />
              </div>

              <div className="form-group">
                <label htmlFor="pclass">Passenger Class</label>
                <select
                  id="pclass"
                  name="pclass"
                  value={formData.pclass}
                  onChange={handleChange}
                  required
                >
                  <option value="">Select Class</option>
                  <option value="1">1st Class</option>
                  <option value="2">2nd Class</option>
                  <option value="3">3rd Class</option>
                </select>
              </div>

              <div className="form-group">
                <label htmlFor="sex">Sex</label>
                <select
                  id="sex"
                  name="sex"
                  value={formData.sex}
                  onChange={handleChange}
                  required
                >
                  <option value="">Select Sex</option>
                  <option value="0">Male</option>
                  <option value="1">Female</option>
                </select>
              </div>

              <div className="form-group">
                <label htmlFor="age">Age</label>
                <input
                  type="number"
                  id="age"
                  name="age"
                  value={formData.age}
                  onChange={handleChange}
                  placeholder="Enter age"
                  min="0"
                  max="120"
                  required
                />
              </div>

              <div className="form-group">
                <label htmlFor="sibsp">Siblings/Spouses</label>
                <input
                  type="number"
                  id="sibsp"
                  name="sibsp"
                  value={formData.sibsp}
                  onChange={handleChange}
                  placeholder="Number of siblings/spouses"
                  min="0"
                  required
                />
              </div>

              <div className="form-group">
                <label htmlFor="parch">Parents/Children</label>
                <input
                  type="number"
                  id="parch"
                  name="parch"
                  value={formData.parch}
                  onChange={handleChange}
                  placeholder="Number of parents/children"
                  min="0"
                  required
                />
              </div>

              <div className="form-group">
                <label htmlFor="fare">Fare (£)</label>
                <input
                  type="number"
                  id="fare"
                  name="fare"
                  value={formData.fare}
                  onChange={handleChange}
                  placeholder="Enter fare amount"
                  min="0"
                  step="0.01"
                  required
                />
              </div>

              <div className="form-group">
                <label htmlFor="embarked">Port of Embarkation</label>
                <select
                  id="embarked"
                  name="embarked"
                  value={formData.embarked}
                  onChange={handleChange}
                  required
                >
                  <option value="">Select Port</option>
                  <option value="1">Cherbourg</option>
                  <option value="0">Queenstown</option>
                  <option value="2">Southampton</option>
                </select>
              </div>
            </div>

            <button type="submit" className="predict-btn" disabled={loading}>
              {loading ? 'Predicting...' : 'Predict Survival'}
            </button>
          </form>

          {prediction && (
            <div className="result-container">
              <div className={`result ${prediction.includes('Survived') ? 'survived' : 'not-survived'}`}>
                <h3>Prediction Result</h3>
                <p className="prediction-text">{prediction}</p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
