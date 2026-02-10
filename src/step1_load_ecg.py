import numpy as np
import os

print("STEP 1 STARTED")

signals = []

for root, _, files in os.walk("data"):
    for f in files:
        if f.endswith(".dat") or f.endswith(".csv"):
            try:
                arr = np.loadtxt(os.path.join(root, f), delimiter=",")
                signals.append(arr.flatten())
            except:
                pass

if len(signals) == 0:
    raise ValueError("No ECG files found in data folder")

ecg = np.concatenate(signals)

np.save("data/ecg_raw.npy", ecg)

print("ECG raw saved")
print("ECG shape:", ecg.shape)
print("STEP 1 FINISHED")
