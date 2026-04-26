from fastapi import FastAPI
from api.schema import CustomerData
from api.model import predict

app = FastAPI()

@app.get("/")
def root():
    return{"message":"FinGuard AI API running"}

@app.post("/predict")
def predict_churn(data: CustomerData):
    result = predict([
        data.tenure,
        data.monthlycharges,
        data.totalcharges,
        data.total_revenue,
        data.avg_monthly_spent
    ])

    return result