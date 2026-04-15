# pandas is used to load and work with the CSV file like a spreadsheet
import pandas as pd
# numpy is used to do mathematical calculations on the data
import numpy as np
# matplotlib is used to draw charts and save them as images
import matplotlib.pyplot as plt


# Load the dataset from CSV
def load_data():
    df = pd.read_csv('cybersecurity_attacks.csv')
    # pd.read_csv opens the CSV file and stores it in 'df' (short for DataFrame)
    # A DataFrame(df) is like an Excel table inside Python

    print("Dataset loaded successfully!")
    # df.shape prints how many rows and columns the dataset has
    print(f"Shape: {df.shape}")
    # df.head() shows the first 5 rows so we can see what the data looks like
    print(f"\nFirst 5 rows:\n{df.head()}")
    # .columns.tolist() prints all 25 column names
    print(f"\nColumn names:\n{df.columns.tolist()}")
    return df

# Clean the data by removing rows with missing values in key columns
def clean_data(df):
    df = df.dropna(subset=['Anomaly Scores', 'Packet Length', 'Attack Type'])
    # dropna means 'drop Not Available' — it removes rows where these columns are empty
    # We only check the 3 most important columns we will use

    print("\nData cleaned!")
    print(f"Rows after cleaning: {len(df)}")
    # len(df) counts how many rows are left after cleaning
    return df

# Calculate and print simple statistics using NumPy and Pandas
def analyze_data(df):
    print("\n--- Simple Statistics ---")
    print(f"Mean Anomaly Score:    {np.mean(df['Anomaly Scores']):.2f}")
    # np.mean calculates the AVERAGE of all anomaly scores
    print(f"Median Anomaly Score:  {np.median(df['Anomaly Scores']):.2f}")
    # np.median finds the MIDDLE value when all scores are sorted
    print(f"Std Dev Anomaly Score: {np.std(df['Anomaly Scores']):.2f}")
    # np.std calculates how SPREAD OUT the scores are
    print(f"Max Packet Length:     {np.max(df['Packet Length'])}")
    # np.max finds the LARGEST packet length 
    print(f"Min Packet Length:     {np.min(df['Packet Length'])}")
    # np.min finds the SMALLEST packet length 
    print("\nAttack Type Counts:")
    print(df['Attack Type'].value_counts())
    # .value_counts() counts how many of each attack type exists
    print("\nSeverity Level Counts:")
    print(df['Severity Level'].value_counts())
    # Same thing for severity — Medium, High and Low are also roughly equal

# Create two visualizations and save them as image files
def visualize_data(df):
    # Visualization 1: Bar chart showing how many of each attack type exist
    plt.figure(figsize=(7, 5))
    df['Attack Type'].value_counts().plot(kind='bar', color=['red', 'blue', 'green'])
     # Counts each attack type and draws them as coloured bars
    # DDoS=red, Malware=blue, Intrusion=green

    plt.title("Attack Type Distribution")
    plt.xlabel("Attack Type")
    plt.ylabel("Count")
    # These three lines add the title and axis labels to the chart
    plt.tight_layout()
    plt.savefig("attack_chart.png")
    # Saves the chart as an image file called attack_chart.png
    plt.show()
    # Displays the chart on screen

    print("\nChart 1 saved as attack_chart.png")
        
    # Visualization 2: Histogram showing the spread of anomaly scores
    plt.figure(figsize=(7, 5))
    plt.hist(df['Anomaly Scores'], bins=30, color='purple', edgecolor='black')
     # plt.hist draws a histogram — it splits the anomaly scores into 30 groups
    # and shows how many scores fall into each group
    plt.title("Distribution of Anomaly Scores")
    plt.xlabel("Anomaly Score")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("anomaly_histogram.png")
    plt.show()
    print("Chart 2 saved as anomaly_histogram.png")
    # Saves and displays the second chart

# Run all functions in order
df = load_data()
#Load the dataset
df = clean_data(df)
#Clean the data
analyze_data(df)
#Print statistics
visualize_data(df)
#: Draw charts