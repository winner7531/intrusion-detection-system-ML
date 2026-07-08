import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import joblib
import json
df = pd.read_csv("archive/Wednesday-workingHours.pcap_ISCX.csv")
df.columns = df.columns.str.strip()
print("Dataset Shape", df.head())
print("\n")
#cleaning
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)
print("Missing Values", df.isnull().sum().sum())

#encoding
le = LabelEncoder()
df["Label"] = le.fit_transform(df["Label"])
print("\n")
print("Label Mapping", dict(zip(le.classes_, le.transform(le.classes_))))
joblib.dump(le, "label_encoder.pkl")

#scaling
X = df.drop("Label", axis=1)
y = df["Label"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
joblib.dump(scaler, "scaler.pkl")

#save files
np.save("X_train.npy", X_train)
np.save("X_test.npy",  X_test)
np.save("y_train.npy", y_train)
np.save("y_test.npy",  y_test)


feature_names = list(df.drop("Label", axis=1).columns)
with open("feature_names.json", "w") as f:
    json.dump(feature_names, f)

print("saved all files.. proceed")