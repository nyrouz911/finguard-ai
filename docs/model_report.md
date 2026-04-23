# Model Report — Churn Prediction

## Model
Logistic Regression

## Performance
- Accuracy: X
- AUC: X
- Precision: X
- Recall: X
## Key Insight
The model struggles with recall for churn prediction, meaning many churners are not detected.

## Improvement Strategy
- Adjust prediction threshold
- Try more complex models (Random Forest, XGBoost)
- Add more behavioral features

## Other Insights
- Monthly charges strongly influence churn
- Tenure impacts retention
- Short-term customers churn more

## Limitations
- simple model
- no hyperparameter tuning
- no advanced features yet

## Threshold Optimization

The default threshold (0.5) led to low recall (~45%), missing many churners.

By lowering the threshold:
- At 0.3 → Recall improved to 90%
- Trade-off: lower precision (more false positives)

## Final Decision

Threshold = 0.3 was selected to maximize business impact by identifying most churners.