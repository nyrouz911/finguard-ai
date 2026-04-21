# Data Model

## Tables

### Customers
- customerID
- demographics
- subscription info
- churn label

### Transactions
- transaction data
- fraud label

### Feedback
- review text
- rating
- sentiment

## Strategy

Datasets are separate:
- They will be treat as parts of the same ecosystem
- The linking will be simulated via:
  - customer segments
  - behavioral patterns

## Future Features

The following features will be created:
- aggregated features (transactions per customer)
- sentiment per customer group
- churn-risk combined indicators