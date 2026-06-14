import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# 1. Load
df = pd.read_csv("phishing_email.csv")
df = df.dropna(subset=["text_combined"])   # drop rows with missing text

# 2. Features (X) and labels (y)
X = df["text_combined"]
y = df["label"]

# 3. Split: 80% train, 20% test. stratify keeps the class balance in both halves.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Turn text into numbers (TF-IDF). Fit on train only, then apply to both.
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# 5. Train the baseline model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# 6. Predict on the held-out test set and evaluate
y_pred = model.predict(X_test_vec)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# 7. Failure analysis: look at the misclassified emails
X_test_reset = X_test.reset_index(drop=True)
y_test_reset = y_test.reset_index(drop=True)
wrong = np.where(y_pred != y_test_reset)[0]

print(f"\nTotal misclassified: {len(wrong)}")
print("\n--- Phishing that slipped through (false negatives) ---")
fn = [i for i in wrong if y_test_reset[i] == 1][:3]
for i in fn:
    print(X_test_reset[i][:200])
    print("---")