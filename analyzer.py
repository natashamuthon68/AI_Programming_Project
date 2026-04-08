import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
def load_data():
    df = pd.read_csv('cybersecurity_attacks.csv')
    print("Dataset loaded successfully!")
    print(f"Shape: {df.shape}")
    print(f"\nFirst 5 rows:\n{df.head()}")
    print(f"\nColumn names:\n{df.columns.tolist()}")
    return df

# Clean the data
def clean_data(df):
    df = df.dropna(subset=['Anomaly Scores', 'Packet Length', 'Attack Type'])
    print("\nData cleaned!")
    print(f"Rows after cleaning: {len(df)}")
    return df

# Basic stats
def analyze_data(df):
    print("\n--- Basic Statistics ---")
    print(f"Mean Anomaly Score: {np.mean(df['Anomaly Scores']):.2f}")
    print(f"Max Packet Length: {np.max(df['Packet Length'])}")
    print(f"Min Packet Length: {np.min(df['Packet Length'])}")
    print("\nAttack Type Counts:")
    print(df['Attack Type'].value_counts())

# Visualization
def visualize_data(df):
    df['Attack Type'].value_counts().plot(kind='bar', color=['red','blue','green'])
    plt.title("Attack Type Distribution")
    plt.xlabel("Attack Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("attack_chart.png")
    plt.show()
    print("\nChart saved as attack_chart.png")

# Run everything
df = load_data()
df = clean_data(df)
analyze_data(df)
visualize_data(df)