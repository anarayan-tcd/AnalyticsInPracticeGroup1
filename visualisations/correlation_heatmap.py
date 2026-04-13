import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import numpy as np

# ── Load ──────────────────────────────────────────────────────────────────────
df = pd.read_csv("/mnt/user-data/uploads/correlation_matrix.csv", index_col=0)

# ── Clean up labels for readability ──────────────────────────────────────────
label_map = {
    "Seniorcitizen":              "Senior citizen",
    "Partner":                    "Partner",
    "Dependents":                 "Dependents",
    "Tenure":                     "Tenure",
    "Phoneservice":               "Phone service",
    "Onlinesecurity":             "Online security",
    "Onlinebackup":               "Online backup",
    "Deviceprotection":           "Device protection",
    "Techsupport":                "Tech support",
    "Streamingtv":                "Streaming TV",
    "Streamingmovies":            "Streaming movies",
    "Paperlessbilling":           "Paperless billing",
    "Monthlycharges":             "Monthly charges",
    "Totalcharges":               "Total charges",
    "Churn":                      "Churn",
    "Has_Streaming":              "Has streaming",
    "Gender:Female":              "Gender: female",
    "Gender:Male":                "Gender: male",
    "MultLines:No":               "Mult. lines: no",
    "MultLines:NoPhoneService":   "Mult. lines: no phone",
    "MultLines:Yes":              "Mult. lines: yes",
    "IntService:Dsl":             "Internet: DSL",
    "IntService:FiberOptic":      "Internet: fiber optic",
    "IntService:No":              "Internet: none",
    "Contract:Month-To-Month":    "Contract: month-to-month",
    "Contract:OneYear":           "Contract: one year",
    "Contract:TwoYear":           "Contract: two year",
    "PayMethod:BankTransfer":     "Payment: bank transfer",
    "PayMethod:CreditCard":       "Payment: credit card",
    "PayMethod:ElectronicCheck":  "Payment: electronic check",
    "PayMethod:MailedCheck":      "Payment: mailed check",
    "OnlineExtras":               "Online extras (sum)",
    "StreamingExtras":            "Streaming extras (sum)",
}

df.index   = [label_map.get(c, c) for c in df.index]
df.columns = [label_map.get(c, c) for c in df.columns]

# ── Reorder: put Churn first, then group by category ─────────────────────────
category_order = [
    "Churn",
    # Demographics
    "Senior citizen", "Partner", "Dependents", "Gender: female", "Gender: male",
    # Account
    "Tenure", "Contract: month-to-month", "Contract: one year", "Contract: two year",
    "Paperless billing", "Monthly charges", "Total charges",
    # Payment
    "Payment: bank transfer", "Payment: credit card",
    "Payment: electronic check", "Payment: mailed check",
    # Services
    "Phone service", "Mult. lines: no", "Mult. lines: no phone", "Mult. lines: yes",
    "Internet: DSL", "Internet: fiber optic", "Internet: none",
    "Online security", "Online backup", "Device protection", "Tech support",
    "Streaming TV", "Streaming movies", "Has streaming",
    "Online extras (sum)", "Streaming extras (sum)",
]

# Keep only cols/rows that exist in the matrix
order = [c for c in category_order if c in df.columns]
df = df.loc[order, order]

# ── Mask: show only lower triangle (removes redundant upper half) ─────────────
mask = np.triu(np.ones_like(df, dtype=bool), k=1)

# ── Color map: red = positive, blue = negative (conventional) ────────────────
cmap = sns.diverging_palette(220, 10, s=80, l=45, as_cmap=True)

# ── Figure ────────────────────────────────────────────────────────────────────
n = len(order)
fig, ax = plt.subplots(figsize=(16, 14))
fig.patch.set_facecolor("#FAFAF8")
ax.set_facecolor("#FAFAF8")

sns.heatmap(
    df,
    mask=mask,
    cmap=cmap,
    vmin=-1, vmax=1,
    center=0,
    square=True,
    linewidths=0.4,
    linecolor="#E8E6DF",
    annot=False,          # set True for value labels (crowded at this size)
    ax=ax,
    cbar_kws={
        "shrink": 0.6,
        "pad": 0.02,
        "ticks": [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1],
        "label": "Pearson r",
    },
)

# ── Axis labels ───────────────────────────────────────────────────────────────
ax.tick_params(axis="x", labelsize=9, rotation=45, labelrotation=45)
ax.tick_params(axis="y", labelsize=9, rotation=0)
ax.set_xticklabels(ax.get_xticklabels(), ha="right", fontsize=9)

# Highlight the Churn row/column label
for label in ax.get_yticklabels():
    if label.get_text() == "Churn":
        label.set_fontweight("bold")
        label.set_color("#993C1D")
for label in ax.get_xticklabels():
    if label.get_text() == "Churn":
        label.set_fontweight("bold")
        label.set_color("#993C1D")

# ── Colorbar styling ──────────────────────────────────────────────────────────
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=9)
cbar.set_label("Pearson r", size=10, labelpad=8)

# ── Category dividers ─────────────────────────────────────────────────────────
# Groups (top→bottom in heatmap): Churn=1, Demographics=5, Account=7, Payment=4, Services=16
# axhline y=0 is bottom; rows are drawn top-to-bottom so divider after row k → y = n-k
dividers = [1, 6, 13, 17]   # cumulative row counts
for d in dividers:
    ax.axhline(y=d,     color="#BFBDB5", linewidth=1.2, linestyle="--", alpha=0.7)
    ax.axvline(x=d,     color="#BFBDB5", linewidth=1.2, linestyle="--", alpha=0.7)

# ── Category annotations (left margin) ────────────────────────────────────────
# y in data coords: 0 = top row, n-1 = bottom row (heatmap draws top→bottom)
groups_annot = [
    (0,  1,   "Churn"),
    (1,  6,   "Demographics"),
    (6,  13,  "Account"),
    (13, 17,  "Payment"),
    (17, n,   "Services"),
]
for y0, y1, name in groups_annot:
    mid = (y0 + y1) / 2
    ax.annotate(
        name,
        xy=(-0.5, mid),
        xycoords=("data", "data"),
        xytext=(-6.8, mid),
        textcoords=("data", "data"),
        fontsize=8.5,
        color="#666",
        va="center",
        ha="right",
        annotation_clip=False,
    )

# ── Title ─────────────────────────────────────────────────────────────────────
ax.set_title(
    "Feature correlation matrix — telco churn dataset",
    fontsize=14,
    fontweight="500",
    pad=18,
    color="#1a1a1a",
    loc="left",
)

ax.set_xlabel("")
ax.set_ylabel("")

plt.tight_layout()
plt.savefig(
    "/mnt/user-data/outputs/correlation_heatmap.png",
    dpi=180,
    bbox_inches="tight",
    facecolor=fig.get_facecolor(),
)
print("Saved.")
