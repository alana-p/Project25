import pandas as pd
import numpy as np
import plotly.express as px

# Load the dataset
input_file = 'dirtydata.csv'
data = pd.read_csv(input_file)

# Inspect the dataset
print(data.head())
print(data.info())

# Clean the dataset: Remove special characters (% * $)
data = data.replace({'[%*$]': ''}, regex=True)

# Drop unnecessary columns
data = data.drop(columns=['Name', 'Extracurricular_Activities'], errors='ignore')

# Output the cleaned data to a new CSV file
output_file = 'cleaned.csv'
data.to_csv(output_file, index=False)
print("The dataset has been cleaned and saved.")

# Define non-numeric columns
non_numeric_cols = ['Gender', 'Department', 'Internet_Access_at_Home', 'Grade']

# Create a dictionary for statistics
stats_dictionary = {}

for col in data.columns:
    if col not in non_numeric_cols:
        stats_data = pd.to_numeric(data[col], errors='coerce')
        
        stats_dictionary[col] = {
            'Mean': stats_data.mean(),
            'Median': stats_data.median(),
            'Mode': stats_data.mode().iloc[0] if not stats_data.mode().empty else np.nan,
            'Range': stats_data.max() - stats_data.min()
        }

print(stats_dictionary)

# Load the cleaned dataset for visualization
df = pd.read_csv(output_file)

# Create the pie chart for Grade Distribution
fig = px.pie(
    df, 
    names='Grade', 
    title='Grade Distribution Among Students', 
    hole=0,  
    color_discrete_sequence=px.colors.sequential.RdBu
)

fig.show()

# Data for Scatter Plot
data = {
    "Study Hours": [6.2, 19, 20.7, 24.8, 15.4, 21.3, 27.3, 8, 9.6, 13.2, 21.3, 18.1, 22.8, 5.8, 25.3, 29.7, 6.2, 17.4, 25.3, 16.9, 19.8, 28, 18.5, 10.9, 23.5, 14.4, 12.1, 11.2],
    "Final Score": [57.82, 45.8, 93.68, 80.63, 78.89, 89.07, 73.96, 90.87, 98.47, 97.43, 91.37, 40.66, 93.14, 44.5, 91.07, 56.81, 76.6, 42.28, 86.27, 46.7, 64.64, 89.05, 81.62, 40.36, 64.18, 42.52, 80.41, 98.14],
    "Attendance": [52.29, 97.27, 5, 95.25, 54.28, 57.60, 51.91, 85.97, 64.01, 85.72, 77.75, 55.44, 96.61, 72.01, 69.51, 83.63, 84.53, 52.30, 66.94, 70.59, 54.84, 19.8, 28, 18.5, 10.9, 23.5, 14.4, 12.1]
}

df = pd.DataFrame(data)

# Scatter Plot
fig = px.scatter(
    df, x="Study Hours", y="Final Score",
    size="Attendance", color="Final Score",
    title="The Effects of Hours Spent Studying on the Final Score",
    labels={"Study Hours": "Hours Studied per Week", "Final Score": "Final Exam Score"},
    hover_data=["Attendance"]
)

fig.show()

