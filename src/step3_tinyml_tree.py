import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from micromlgen import port
import os

print("Loading ECG features...")

df = pd.read_csv("data/ecg_features.csv")

X = df.drop("label", axis=1).values
y = df["label"].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training TinyML Decision Tree...")

model = DecisionTreeClassifier(
    max_depth=4,
    min_samples_leaf=20,
    random_state=42
)

model.fit(X_train, y_train)

acc = model.score(X_test, y_test)
print("ECG TinyML Accuracy:", acc)

os.makedirs("models", exist_ok=True)

with open("models/ecg_tinyml_model.h", "w") as f:
    f.write(port(model))

print("SUCCESS ECG TinyML model saved")
