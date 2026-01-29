import numpy as np
import pandas as pd

print("Loading raw ECG signal...")
signal = np.load("data/ecg_raw.npy")

window = 200
features = []
labels = []

# Simple proxy label (mean-based)
threshold = np.mean(signal)

print("Extracting features...")

for i in range(0, len(signal) - window, window):
    seg = signal[i:i+window]

    feat = [
        np.mean(seg),
        np.std(seg),
        np.min(seg),
        np.max(seg),
        np.ptp(seg),   # peak-to-peak
        np.var(seg)
    ]

    label = 1 if np.mean(seg) > threshold else 0

    features.append(feat)
    labels.append(label)

df = pd.DataFrame(features, columns=[
    "mean", "std", "min", "max", "ptp", "var"
])
df["label"] = labels

df.to_csv("data/ecg_features.csv", index=False)

print("ECG feature file saved")
print("Feature shape:", df.shape)
