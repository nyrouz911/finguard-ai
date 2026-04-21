import pandas as pd
import sys
sys.path.append("../src")
from db_connection import get_engine

engine = get_engine()

# Load datasets
customers = pd.read_csv("data/raw/customers.csv")
transactions = pd.read_csv("data/raw/transactions.csv")
feedback = pd.read_csv("data/raw/feedback.csv")

# Push to PostgreSQL
customers.to_sql("raw_customers", engine, if_exists="replace", index=False)
transactions.to_sql("raw_transactions", engine, if_exists="replace", index=False)
feedback.to_sql("raw_feedback", engine, if_exists="replace", index=False)

print("Data loaded into PostgreSQL ✅")