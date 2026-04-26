from pydantic import BaseModel

class CustomerData(BaseModel):
    tenure:float
    monthlycharges:float
    totalcharges: float
    total_revenue: float
    avg_monthly_spent: float