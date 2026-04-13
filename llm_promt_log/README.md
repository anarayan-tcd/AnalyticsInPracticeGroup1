### Log Entry 1: Data Pipeline Critique
| Field | Details |
|-------|---------|
| **Objective** | Ensure the data engineering pipeline is robust, reproducible, and handles data quality issues |
| **Input** | DataCleanPipeline.py |
| **AI Tool** | Gemini 1.5 Pro |
| **Key Findings** | pd.to_numeric(errors='coerce') confirmed as safe for TotalCharges handling. Pipeline is well-modularised. |
| **Audit Point 1 (Technical)** | Missing Feature Scaling — StandardScaler recommended for Logistic Regression |
| **Audit Point 2 (Business)** | No automated Outlier Detection — extreme billing anomalies should be flagged |

---

### Log Entry 2: Model Reliability Assessment
| Field | Details |
|-------|---------|
| **Objective** | Evaluate predictive power of Logistic Regression and identify performance risks |
| **Input** | logistic_regression_results.csv |
| **AI Tool** | Gemini 1.5 Pro |
| **Key Finding** | Recall score of 0.51 for churn class means ~49% of churners are missed — significant business risk |
| **Business Implication** | False negatives = customers who churn without being flagged — direct revenue loss |

---

### Log Entry 3: Insight Synthesis for Recommendations
| Field | Details |
|-------|---------|
| **Objective** | Convert model coefficients into CEO-ready business strategies |
| **Input** | logistic_regression_results.csv coefficients |
| **AI Tool** | Gemini 1.5 Pro |
| **Driver 1** | Fiber Optic (highest churn risk) → Launch "Fiber Loyalty Credit" |
| **Driver 2** | Month-to-Month Contracts → Offer "Contract Anniversary Bonuses" from month 6 |
| **Driver 3** | Online Security (retention anchor) → Bundle as free add-on in high-risk plans |
| **Audit Point 1 (Business)** | Recommendations assume causality — A/B test required to prove security causes retention |
| **Audit Point 2 (Technical)** | Interaction effects ignored — Fiber + Senior Citizen may create even higher risk profile |

---

### Additional AI Use (Aditya)
| Field | Details |
|-------|---------|
| **Prompt** | "Create a nice graphic to show the following cluster data clearly: [cluster output from Python]" |
| **AI Tool** | Claude |
| **Output** | Cluster visualisation graphic of 5 churner profiles |
| **Assessment** | Accurate and useful — graphic clearly displayed cluster groupings for analysis |

| Field | Details |
|-------|---------|
| **Prompt** | "Put 20 rows of customer data where churn = yes into a csv file. Also add another 20 rows where the customer would NOT churn. Based on the code sent above, all columns that aren't charges related should be 0 or 1.
| **AI Tool** | Claude |
| **Output** | churn_sample_data.csv — 40 synthetic customer entries (20 churn, 20 no churn) |
| **Assessment** | With some re-prompting and explaining, Claude created a decent sample set of 40 data entries based on clustering results |

*All AI-generated content reviewed and verified by the team. GenAI use acknowledged per TCD guidelines.*
