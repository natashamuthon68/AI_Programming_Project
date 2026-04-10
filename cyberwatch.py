import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Title of the web app
st.title("🔐 Cybersecurity Attacks Analyzer")
st.write("This app analyzes a cybersecurity attacks dataset and predicts attack types using a Decision Tree model.")

# Load data
df = pd.read_csv("cybersecurity_attacks.csv")
st.subheader("📊 Raw Dataset")
st.write(f"Total rows: {len(df)}")
st.dataframe(df.head(10))

# Simple stats
st.subheader("📈 Simple Statistics")
st.write(f"**Mean Anomaly Score:** {np.mean(df['Anomaly Scores']):.2f}")
st.write(f"**Max Packet Length:** {np.max(df['Packet Length'])}")
st.write(f"**Min Packet Length:** {np.min(df['Packet Length'])}")

# Chart 1: Attack type bar chart
st.subheader("⚔️ Attack Type Distribution")
fig1, ax1 = plt.subplots()
df['Attack Type'].value_counts().plot(kind='bar', color=['red','blue','green'], ax=ax1)
ax1.set_xlabel("Attack Type")
ax1.set_ylabel("Count")
st.pyplot(fig1)

# Chart 2: Anomaly scores histogram
st.subheader("📉 Anomaly Score Distribution")
fig2, ax2 = plt.subplots()
ax2.hist(df['Anomaly Scores'], bins=30, color='purple', edgecolor='black')
ax2.set_xlabel("Anomaly Score")
ax2.set_ylabel("Frequency")
st.pyplot(fig2)

# ML Model
st.subheader(" Decision Tree — Attack Type Predictor")
features = ['Packet Length', 'Anomaly Scores', 'Source Port', 'Destination Port']
X = df[features]
le = LabelEncoder()
y = le.fit_transform(df['Attack Type'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
st.write(f"**Model Accuracy:** {accuracy * 100:.2f}%")
st.write("**Note:** Low accuracy is because the dataset is synthetic — no real patterns exist in the data.")