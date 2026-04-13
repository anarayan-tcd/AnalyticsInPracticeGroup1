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

---

### Additional AI Use (Nadia — Visualisations)

All visualisation prompts were run in Google Colab using Gemini, 
with final dashboard compilation done in Claude.

| # | Prompt | Tool | Output |
|---|--------|------|--------|
| 1 | "Find 4 KPIs: overall churn rate, highest risk segment, fiber optic churn, e-check churn" | Gemini | KPI tiles for churn overview dashboard |
| 2 | "Create bar charts for churn rate by contract type, internet service, payment method, and tenure band" | Gemini | 4 individual bar charts |
| 3 | "Compile all of the above into an HTML dashboard" | Gemini | dashboard_1_churn_overview.html |
| 4 | "Create a diverging bar chart showing feature correlation with churn, sorted by strength" | Gemini | Correlation chart |
| 5 | "Create a feature correlation matrix using lower triangle only, grouped by category" | Gemini | correlation_heatmap.png |
| 6 | "Create a metric heatmap and bubble chart for each of the 5 customer clusters" | Gemini | dashboard_3_clusters.html |
| 7 | "Find 4 KPIs: accuracy, churn precision, churn recall, F1 score" | Gemini | KPI tiles for model performance dashboard |
| 8 | "Create confusion matrix, grouped bar chart and feature coefficients chart" | Gemini | dashboard_4_model_performance.html |
| 9 | "Compile all visualisations into 5 separate HTML dashboards" | Claude | 5 interactive HTML dashboards |
| 10 | "Use tooltips/hover states instead of static labels" | Claude | Final polished dashboards |

*All AI-generated content reviewed and verified by the team. GenAI use acknowledged per TCD guidelines.*
