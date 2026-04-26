import joblib
import numpy as np

model= joblib.load("api/model.joblib")

def predict(data):
    data_array = np.array(data).reshape(1,-1)
    proba = model.predict_proba(data_array)[0][1]

    prediction = int(proba>0.3) #used the best threshold

    return{
        "prediction" : prediction,
        "probability": float(proba)
    }