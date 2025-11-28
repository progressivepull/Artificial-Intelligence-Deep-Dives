import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score, precision_recall_curve, auc
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.calibration import CalibratedClassifierCV
from sklearn.utils.class_weight import compute_class_weight

# 1) Load data
df = pd.read_csv("hospital_readmission_dataset.csv")

# 2) Features and target
features = ["prior_visits_last_year", "age", "chronic_conditions"]
X = df[features]
y = df["readmitted_30_days"]

# 3) Train/test split (stratified)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# 4) Baseline: predict majority class
baseline_pred = np.zeros_like(y_test)  # assume '0' is majority
print("Baseline classification report:")
print(classification_report(y_test, baseline_pred, digits=3))

# 5) Class weights for imbalance
classes = np.unique(y)
class_weights = compute_class_weight(class_weight="balanced", classes=classes, y=y)
cw = {int(c): w for c, w in zip(classes, class_weights)}
print("Class weights:", cw)

# 6) Interpretable model: Logistic Regression
logit_pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(
        class_weight=cw, 
        max_iter=2000, 
        solver="lbfgs", 
        C=1.0
    ))
])

logit_pipe.fit(X_train, y_train)
logit_proba = logit_pipe.predict_proba(X_test)[:, 1]
logit_pred = (logit_proba >= 0.5).astype(int)

print("\nLogistic Regression classification report:")
print(classification_report(y_test, logit_pred, digits=3))
print("Logistic ROC-AUC:", roc_auc_score(y_test, logit_proba))

# Optional: choose threshold by maximizing F1 or Youden’s J on validation
prec, rec, th = precision_recall_curve(y_test, logit_proba)
f1 = 2 * (prec * rec) / (prec + rec + 1e-9)
best_idx = np.nanargmax(f1)
best_threshold = th[best_idx] if best_idx < len(th) else 0.5
print("Best threshold (by F1):", round(float(best_threshold), 3))

# 7) Stronger model: Gradient Boosting + probability calibration
gb = GradientBoostingClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=3,
    random_state=42
)
gb_cal = CalibratedClassifierCV(gb, cv=5, method="isotonic")
gb_cal.fit(X_train, y_train)
gb_proba = gb_cal.predict_proba(X_test)[:, 1]
gb_pred = (gb_proba >= best_threshold).astype(int)

print("\nGradient Boosting classification report (using best threshold):")
print(classification_report(y_test, gb_pred, digits=3))
print("Gradient Boosting ROC-AUC:", roc_auc_score(y_test, gb_proba))

# 8) Feature importance (GBM)
importances = gb.feature_importances_ if hasattr(gb, "feature_importances_") else None
if importances is not None:
    fi = pd.Series(importances, index=features).sort_values(ascending=False)
    print("\nGradient Boosting feature importances:")
    print(fi)

# 9) Produce patient-level risk scores and predictions for the full dataset
df["risk_logit"] = logit_pipe.predict_proba(X)[:, 1]
df["risk_gb"] = gb_cal.predict_proba(X)[:, 1]
df["pred_logit"] = (df["risk_logit"] >= best_threshold).astype(int)
df["pred_gb"] = (df["risk_gb"] >= best_threshold).astype(int)

# 10) Save outputs
df_out = df[["patient_id"] + features + ["readmitted_30_days", "risk_logit", "risk_gb", "pred_logit", "pred_gb"]]
df_out.to_csv("readmission_predictions.csv", index=False)
print("\nSaved: readmission_predictions.csv")
