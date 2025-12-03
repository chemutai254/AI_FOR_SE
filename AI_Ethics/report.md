## **Racial Bias Analysis of COMPAS Dataset**
## Objective
- To analyzed the COMPAS recidivism risk score dataset for racial bias using IBM's AI Fairness 360 (AIF360) toolkit.
Data Source: [COMPAS Recidivism Data](https://www.propublica.org/datastore/dataset/compas-recidivism-risk-score-data-and-analysis)

## Activities
- *Data Loading*: Manually loaded the compas-scores-two-years.csv dataset and performed preprocessing to filter invalid entries and encode categorical variables.
- *Fairness Metric Calculation*: Used BinaryLabelDataset and ClassificationMetric from AIF360 to compute fairness metrics.
- *Risk Score Analysis*: Instead of training a new model, I analyzed the existing COMPAS risk scores (decile_score) by treating scores >= 5 as a prediction of "High/Medium Risk" (recidivism).
- *Visualization*: Added a bar chart to visualize the disparity in False Positive Rates between African-American and Caucasian groups.
Verification Results
I verified the analysis by running the code and checking the computed metrics.

Key Findings
False Positive Rate (African-American): ~0.42
False Positive Rate (Caucasian): ~0.22
Difference: ~0.20
This confirms that African-American defendants are significantly more likely to be falsely flagged as high risk compared to Caucasian defendants, which aligns with the known bias in the COMPAS dataset.

Visualization
The notebook generates a bar chart showing this disparity:

FPR Visualization (Note: The notebook generates a similar plot dynamically)