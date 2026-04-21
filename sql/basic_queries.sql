-- Check row counts
SELECT COUNT(*) FROM raw_customers;
SELECT COUNT(*) FROM raw_transactions;
SELECT COUNT(*) FROM raw_feedback;

-- Check churn distribution
SELECT "Churn", COUNT(*) 
FROM raw_customers
GROUP BY "Churn";

-- Check fraud distribution
SELECT "Class", COUNT(*)
FROM raw_transactions
GROUP BY "Class";