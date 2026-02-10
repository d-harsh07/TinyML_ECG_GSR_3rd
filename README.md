# TinyML EEG + GSR Stress Classification

## Overview
This project implements a TinyML-based multimodal stress classification system using EEG and GSR signals from the Young Adults Affective dataset.

## Methodology
- EEG and GSR signals loaded from nested directories
- Statistical feature extraction using sliding windows
- Early feature-level fusion
- Lightweight Decision Tree model
- Exported as C header for edge deployment

## Model Details
- Algorithm: Decision Tree (TinyML)
- Fusion: Early (feature-level)
- Output: `models/eeg_gsr_tinyml_model.h`

## Tools
- Python
- scikit-learn
- micromlgen
- VS Code

## Note
Raw datasets are excluded from version control due to size constraints.
