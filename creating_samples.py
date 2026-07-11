import pandas as pd
import json
import os

# Load dataset
df = pd.read_csv("archive/Wednesday-workingHours.pcap_ISCX.csv")

# Remove any extra spaces in column names
df.columns = df.columns.str.strip()

# Create folder for samples
os.makedirs("sample_jsons", exist_ok=True)

# Get all unique labels
labels = df["Label"].unique()

for label in labels:
    # Take first sample of this class
    sample = df[df["Label"] == label].iloc[0]

    # Remove label column
    features = sample.drop("Label")

    # Safe filename
    filename = (
        label.replace("/", "_")
             .replace(" ", "_")
             .replace(":", "_")
             .replace("�", "")
    )

    # Save JSON
    with open(f"sample_jsons/{filename}.json", "w") as f:
        json.dump(features.to_dict(), f, indent=2)

    print(f"Saved {filename}.json")

print("Done!")