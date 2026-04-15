import pandas as pd
# Used to load the dataset
from sklearn.tree import DecisionTreeClassifier
# The main ML model we are using — a Decision Tree
from sklearn.model_selection import train_test_split
# Used to split data into training and testing sets
from sklearn.preprocessing import LabelEncoder
# Used to convert text labels (DDoS, Malware) into numbers (0, 1, 2)
# because ML models only understand numbers
from sklearn.metrics import accuracy_score, classification_report
# Used to measure how well the model performed


# Step 1: Load the dataset
#Opens the CSV file and loads it into Python so we can work with it
def load_data():
    df = pd.read_csv('cybersecurity_attacks.csv')
    # Loads all 40,000 rows into a DataFrame
    print("Dataset loaded successfully!")
    print(f"Total rows: {len(df)}")
    return df

# Step 2: Prepare features (X) and target (y) for the model
def prepare_data(df):
    # These are the input columns the model will learn from
    features = ['Packet Length', 'Anomaly Scores', 'Source Port', 'Destination Port']
    target = 'Attack Type'
    # Packet Length = size of the network packet in bytes
    # Anomaly Score = how suspicious the traffic looks (0-100)
    # Source/Destination Port = which ports are being used


    X = df[features]
    # X holds all the input data
    y = df[target]
    # y holds all the correct answers

    # Encode target labels from text to numbers (e.g. DDoS=0, Intrusion=1, Malware=2)
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    # le.fit_transform learns all unique labels and converts them to numbers at once
    # We do this because ML models only work with numbers, not text

    print(f"\nFeatures used: {features}")
    print(f"Target classes: {list(le.classes_)}")
    # le.classes converts the number back to the text label
    return X, y_encoded, le

# Step 3: Split data into training and testing sets
def split_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    # test_size=0.2 means 20% goes to testing, 80% goes to training
    # So: 32,000 rows for training, 8,000 rows for testing
    # random_state=42 makes sure we get the same split every time we run
    # Think of it like: study 80% of past papers, test on the remaining 20%

    print(f"\nTraining samples: {len(X_train)}")
    print(f"Testing samples:  {len(X_test)}")
    return X_train, X_test, y_train, y_test

# Step 4: Train the Decision Tree model
def train_model(X_train, y_train):
    # max_depth=5 limits how deep the tree grows to avoid overfitting
    model = DecisionTreeClassifier(max_depth=5, random_state=42)
    # Creates a Decision Tree model
    # max_depth=5 means the tree can only make 5 levels of decisions
    # This prevents overfitting — where the model memorizes answers instead of learning

    model.fit(X_train, y_train)
    # .fit() is the training step we show the model 32,000 examples
    # and it learns the patterns between the features and attack types

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
    # Loop through the first 10 predictions and print them
    # We compare what the model guessed vs what the correct answer was

        a_label = le.classes_[actual]
        p_label = le.classes_[predicted]
        correct = "Yes" if actual == predicted else "No"
        print(f"{a_label:<12} {p_label:<12} {correct}")

    # Calculate and print accuracy
    accuracy = accuracy_score(y_test, y_pred)
    # accuracy_score calculates: correct predictions / total predictions
    # Result: 33% — this is expected because the dataset is fake

    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

    # Full evaluation breakdown per class
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=le.classes_))
    # classification_report shows detailed results for each attack type
    # including precision (how often it was right) and recall (how many it caught)


    # Explain why accuracy is low
    print("Note: The low accuracy is due to the dataset being synthetically generated.")
    print("The data does not have real patterns linking features to attack types.")

# Run all steps in order
df = load_data()
X, y, le = prepare_data(df)
X_train, X_test, y_train, y_test = split_data(X, y)
model = train_model(X_train, y_train)
evaluate_model(model, X_test, y_test, le)
