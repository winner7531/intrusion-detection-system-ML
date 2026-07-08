import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
import joblib
#load
def load_data():
    X_train = np.load("X_train.npy")
    X_test = np.load("X_test.npy")
    y_train = np.load("y_train.npy")
    y_test = np.load("y_test.npy")
    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = load_data()

#train
def train(X_train, y_train):
    print("training radnom forest")
    model = RandomForestClassifier(
        n_estimators=100,
        #max_depth=20,
        n_jobs=-1,              
        random_state=42,
        class_weight="balanced", 
    )
    model.fit(X_train, y_train)
    print("Training complete!")

    return model
model = train(X_train, y_train)

#evaluation metrics
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
#print(confusion_matrix(y_test, y_pred))

#saving the model
joblib.dump(model, "model.pkl")