import pandas as pd
import numpy as np
from flask import Flask, render_template, request
import pickle

# Initialize app
app = Flask(__name__)

# Load data and model
data = pd.read_csv("Cleaned_data.csv")
pipe = pickle.load(open("LinearRegression.pkl", "rb"))

# Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)


# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        location = request.form.get('location')
        bhk = int(request.form.get('bhk'))
        bath = int(request.form.get('bath'))
        sqft = float(request.form.get('total_sqft'))

        # Create dataframe
        input_df = pd.DataFrame([[location, sqft, bath, bhk]],
                                columns=['location', 'total_sqft', 'bath', 'bhk'])

        # Prediction
        prediction = pipe.predict(input_df)[0] * 1e5

        # Return result
        return str(np.round(prediction, 2))

    except Exception as e:
        return f"Error: {str(e)}"


# Run app
if __name__ == "__main__":
    app.run(debug=True, port=5001, use_reloader=False)