
from flask import Flask, request, render_template
import pickle
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
#import lightgbm as lgb

app = Flask(__name__)

# Load model, encoder, scaler
#model = pickle.load(open("xgb_model.pkl", "rb"))
model = XGBClassifier()
model.load_model("xgb.json")
encoder = pickle.load(open("encoder.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html", prediction_text=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        balance = int(request.form['balance'])
        duration = int(request.form['duration'])
        pdays = int(request.form['pdays'])
        previous = int(request.form['previous'])
        education = request.form['education']

        education_encoded = encoder.transform([[education]])[0][0]

        input_df = pd.DataFrame([[balance, duration, pdays, previous, education_encoded]],
                                columns=["balance", "duration", "pdays", "previous", "education"])

        prediction = model.predict(input_df)[0]
        result = "Client  will subscribe term deposit" if prediction == 1 else "Client will not subscribe term deposit"

        # Return with fresh prediction
        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)
