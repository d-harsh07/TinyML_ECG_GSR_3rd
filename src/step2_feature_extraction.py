print("STEP 2 STARTED")

import numpy as np
import pandas as pd

ecg = np.load("data/ecg_raw.npy")

window = 200
features = []
labels = []

threshold = np.mean(ecg)

for i in range(0, len(ecg) - window, window):
    seg = ecg[i:i+window]

    feat = [
        np.std(seg),
        np.ptp(seg),
        np.var(seg)
    ]

    label = 1 if np.mean(seg) > threshold else 0

    features.append(feat)
    labels.append(label)

df = pd.DataFrame(features, columns=["std", "ptp", "var"])
df["label"] = labels

df.to_csv("data/ecg_features.csv", index=False)

print("ECG features saved")
print("Shape:", df.shape)
print("STEP 2 FINISHED")
