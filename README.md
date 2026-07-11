# Intrusion Detection System (IDS)

Machine Learning based Intrusion Detection System built using the CICIDS2017 dataset.

## Overview

This project detects and classifies network traffic into benign and attack categories using a Random Forest classifier.

Current attack classes:

- BENIGN
- DoS Hulk
- DoS GoldenEye
- DoS Slowloris
- DoS Slowhttptest
- Heartbleed

## Features

- Data cleaning and preprocessing
- Label encoding
- Feature scaling
- Random Forest classification
- Feature importance analysis
- Model serialization using Joblib
- Ready for Flask deployment
- Working flask dashboard

## Dataset

Dataset: CICIDS2017

Current training file:

- Whole CICIDS2017 dataset

## Project Structure

```text
IDS/
├── preprocessing.py
├── train.py
├── visualize.py
├── scaler.pkl
├── label_encoder.pkl
├── feature_names.json
├── model.pkl
└── archive/
```

## Results

Accuracy: 99.93%

Classification Metrics:

- Precision: ~1.00
- Recall: ~1.00
- F1 Score: ~1.00

### Feature Importance

Top contributing features include:

- Max Packet Length
- Bwd Packet Length Max
- Total Length of Bwd Packets
- Flow IAT Mean


## Installation

```bash
pip install pandas numpy scikit-learn matplotlib joblib
```

## Usage

### Preprocess Data

```bash
python preprocessing.py
```

### Train Model

```bash
python train.py
```

### Generate Visualizations

```bash
python visualize.py
```

## Future Improvements

- Real-time traffic classification
- Compare Random Forest with XGBoost and other models
- Improved handling of class imbalance

## Author

Shikhar Gautam
