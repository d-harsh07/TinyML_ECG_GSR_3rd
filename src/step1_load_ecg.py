import numpy as np
import os

data_root = "data"
signals = []
ecg_files = []

# Walk through all subfolders to find ECG files
for root, dirs, files in os.walk(data_root):
    for file in files:
        if file.lower().endswith(".dat"):
            ecg_files.append(os.path.join(root, file))

print(f"Total ECG files found: {len(ecg_files)}")

if len(ecg_files) == 0:
    raise ValueError("No ECG .dat files found. Check folder structure.")

# Load ECG signals
for file in ecg_files:
    try:
        signal = np.loadtxt(file, delimiter=",")
        signal = signal.flatten()
        signals.append(signal)
    except Exception as e:
        print(f"Skipping {file} due to error: {e}")

# Concatenate all signals
signals = np.concatenate(signals)

# Save combined ECG signal
np.save("data/ecg_raw.npy", signals)

print("ECG raw signal loaded successfully")
print("Final ECG signal shape:", signals.shape)
