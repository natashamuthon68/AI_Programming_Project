import streamlit as st
# streamlit is used to build and display the interactive web app in the browser
import pandas as pd
# pandas is used to load the dataset
import numpy as np
# numpy is used for mathematical calculations
import matplotlib.pyplot as plt
# matplotlib is used to create charts and visualizations
from sklearn.tree import DecisionTreeClassifier
# DecisionTreeClassifier is the ML model we use to predict attack types
from sklearn.model_selection import train_test_split
# train_test_split splits the data into 80% training and 20% testing
from sklearn.preprocessing import LabelEncoder
# LabelEncoder converts text labels like DDoS and Malware into numbers
from sklearn.metrics import accuracy_score, classification_report
# accuracy_score measures how many predictions the model got correct
# classification_report gives a detailed breakdown of model performance

# Title of the web app
st.title("Cybersecurity Attacks Analyzer")
st.write("This app analyzes a cybersecurity attacks dataset and predicts attack types using a Decision Tree model.")
# st.write displays text on the web page

df = pd.read_csv("cybersecurity_attacks.csv")
st.subheader(" Raw Dataset")
# st.subheader displays a smaller heading
st.write(f"Total rows: {len(df)}")
# len(df) counts the total number of rows in the dataset
st.dataframe(df.head(10))
# st.dataframe displays the first 10 rows as an interactive table

# Simple statistics
st.subheader(" Simple Statistics")
st.write(f"**Mean Anomaly Score:** {np.mean(df['Anomaly Scores']):.2f}")
# np.mean calculates the average of all anomaly scores
st.write(f"**Max Packet Length:** {np.max(df['Packet Length'])}")
# np.max finds the largest packet length in the dataset
st.write(f"**Min Packet Length:** {np.min(df['Packet Length'])}")

# Chart 1: Attack type bar chart
st.subheader("Attack Type Distribution")
fig1, ax1 = plt.subplots()
# plt.subplots creates a blank figure and axes to draw on
df['Attack Type'].value_counts().plot(kind='bar', color=['red','blue','green'], ax=ax1)
# value_counts counts each attack type, plot draws it as a bar chart
ax1.set_xlabel("Attack Type")
ax1.set_ylabel("Count")
st.pyplot(fig1)
# st.pyplot displays the matplotlib chart inside the Streamlit app

# Chart 2: Anomaly scores histogram
st.subheader("Anomaly Score Distribution")
fig2, ax2 = plt.subplots()
# ax2.hist draws a histogram splits scores into 30 groups and shows frequency
ax2.hist(df['Anomaly Scores'], bins=30, color='purple', edgecolor='black')
ax2.set_xlabel("Anomaly Score")
ax2.set_ylabel("Frequency")
st.pyplot(fig2)

# ML Model
st.subheader(" Decision Tree — Attack Type Predictor")
features = ['Packet Length', 'Anomaly Scores', 'Source Port', 'Destination Port']
# Select the input columns the model will use to make predictions
X = df[features]
le = LabelEncoder()
# LabelEncoder converts text labels DDoS, Malware into numbers 
y = le.fit_transform(df['Attack Type'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Split data 80% for training, 20% for testing
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)
# Create and train the Decision Tree model with max 5 levels
y_pred = model.predict(X_test)
# predict() makes the model guess attack types for the test rows
accuracy = accuracy_score(y_test, y_pred)
# accuracy_score calculates how many predictions were correct
st.write(f"**Model Accuracy:** {accuracy * 100:.2f}%")
st.write("**Note:** Low accuracy is because the dataset is synthetic — no real patterns exist in the data.")
# Note explaining why accuracy is low