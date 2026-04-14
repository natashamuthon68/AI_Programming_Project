import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the dataset from CSV
def load_data():
    df = pd.read_csv('cybersecurity_attacks.csv')
    print("Dataset loaded successfully!")
    print(f"Shape: {df.shape}")
    print(f"\nFirst 5 rows:\n{df.head()}")
    print(f"\nColumn names:\n{df.columns.tolist()}")
    return df

# Clean the data by removing rows with missing values in key columns
def clean_data(df):
    df = df.dropna(subset=['Anomaly Scores', 'Packet Length', 'Attack Type'])
    print("\nData cleaned!")
    print(f"Rows after cleaning: {len(df)}")
    return df

# Calculate and print simple statistics using NumPy and Pandas
def analyze_data(df):
    print("\n--- Simple Statistics ---")
    print(f"Mean Anomaly Score:    {np.mean(df['Anomaly Scores']):.2f}")
    print(f"Median Anomaly Score:  {np.median(df['Anomaly Scores']):.2f}")
    print(f"Std Dev Anomaly Score: {np.std(df['Anomaly Scores']):.2f}")
    print(f"Max Packet Length:     {np.max(df['Packet Length'])}")
    print(f"Min Packet Length:     {np.min(df['Packet Length'])}")
    print("\nAttack Type Counts:")
    print(df['Attack Type'].value_counts())
    print("\nSeverity Level Counts:")
    print(df['Severity Level'].value_counts())

# Create two visualizations and save them as image files
def visualize_data(df):
    # Visualization 1: Bar chart showing how many of each attack type exist
    plt.figure(figsize=(7, 5))
    df['Attack Type'].value_counts().plot(kind='bar', color=['red', 'blue', 'green'])
    plt.title("Attack Type Distribution")
    plt.xlabel("Attack Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("attack_chart.png")
    plt.show()
    print("\nChart 1 saved as attack_chart.png")

    # Visualization 2: Histogram showing the spread of anomaly scores
    plt.figure(figsize=(7, 5))
    plt.hist(df['Anomaly Scores'], bins=30, color='purple', edgecolor='black')
    plt.title("Distribution of Anomaly Scores")
    plt.xlabel("Anomaly Score")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("anomaly_histogram.png")
    plt.show()
    print("Chart 2 saved as anomaly_histogram.png")

# Run all functions in order
df = load_data()
df = clean_data(df)
analyze_data(df)
visualize_data(df)
