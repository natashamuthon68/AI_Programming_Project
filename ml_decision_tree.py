import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load the dataset
def load_data():
    df = pd.read_csv('cybersecurity_attacks.csv')
    print("Dataset loaded successfully!")
    print(f"Total rows: {len(df)}")
    return df

# Step 2: Prepare features (X) and target (y) for the model
def prepare_data(df):
    # These are the input columns the model will learn from
    features = ['Packet Length', 'Anomaly Scores', 'Source Port', 'Destination Port']
    target = 'Attack Type'

    X = df[features]
    y = df[target]

    # Encode target labels from text to numbers (e.g. DDoS=0, Intrusion=1, Malware=2)
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    print(f"\nFeatures used: {features}")
    print(f"Target classes: {list(le.classes_)}")
    return X, y_encoded, le

# Step 3: Split data into training and testing sets
def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"\nTraining samples: {len(X_train)}")
    print(f"Testing samples:  {len(X_test)}")
    return X_train, X_test, y_train, y_test

# Step 4: Train the Decision Tree model
def train_model(X_train, y_train):
    # max_depth=5 limits how deep the tree grows to avoid overfitting
    model = DecisionTreeClassifier(max_depth=5, random_state=42)
    model.fit(X_train, y_train)
    print("\nModel trained successfully!")
    return model

# Step 5: Make predictions and evaluate the model
def evaluate_model(model, X_test, y_test, le):
    # Use the trained model to predict attack types on unseen test data
    y_pred = model.predict(X_test)

    # Print sample predictions vs actual values
    print("\n--- Sample Predictions (first 10) ---")
    print(f"{'Actual':<12} {'Predicted':<12} {'Correct?'}")
    print("-" * 36)
    for actual, predicted in zip(y_test[:10], y_pred[:10]):
        a_label = le.classes_[actual]
        p_label = le.classes_[predicted]
        correct = "Yes" if actual == predicted else "No"
        print(f"{a_label:<12} {p_label:<12} {correct}")

    # Calculate and print accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

    # Full evaluation breakdown per class
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=le.classes_))

    # Explain why accuracy is low
    print("Note: The low accuracy is due to the dataset being synthetically generated.")
    print("The data does not have real patterns linking features to attack types.")

# Run all steps in order
df = load_data()
X, y, le = prepare_data(df)
X_train, X_test, y_train, y_test = split_data(X, y)
model = train_model(X_train, y_train)
evaluate_model(model, X_test, y_test, le)
