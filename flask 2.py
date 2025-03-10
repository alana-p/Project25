from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio  

app = Flask(__name__)

# Load the CSV file
file_path = "cleaned.csv"
try:
    df_csv = pd.read_csv(file_path)
    if "Grade" not in df_csv.columns:
        print("Error: 'Grade' column not found. Check column names:", df_csv.columns)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")

# Create Pie Chart for Grade Distribution
fig_pie = px.pie(
    df_csv, 
    names='Grade',  
    title='Grade Distribution Among Students', 
    hole=0,  
    color_discrete_sequence=px.colors.sequential.RdBu
)

graph_html_pie = pio.to_html(fig_pie, full_html=False)

# Sample Scatter Plot Data
data = {
    "Study Hours": [6.2, 19, 20.7, 24.8, 15.4, 21.3, 27.3, 8, 9.6, 13.2, 21.3, 18.1, 22.8, 5.8, 25.3, 29.7, 6.2, 17.4, 25.3, 16.9, 19.8, 28, 18.5, 10.9, 23.5, 14.4, 12.1, 11.2],
    "Final Score": [57.82, 45.8, 93.68, 80.63, 78.89, 89.07, 73.96, 90.87, 98.47, 97.43, 91.37, 40.66, 93.14, 44.5, 91.07, 56.81, 76.6, 42.28, 86.27, 46.7, 64.64, 89.05, 81.62, 40.36, 64.18, 42.52, 80.41, 98.14],
    "Attendance": [52.29, 97.27, 5, 95.25, 54.28, 57.60, 51.91, 85.97, 64.01, 85.72, 77.75, 55.44, 96.61, 72.01, 69.51, 83.63, 84.53, 52.30, 66.94, 70.59, 54.84, 19.8, 28, 18.5, 10.9, 23.5, 14.4, 12.1]
}

df = pd.DataFrame(data)

# Create Scatter Plot
fig_scatter = px.scatter(
    df, x="Study Hours", y="Final Score",
    size="Attendance", color="Final Score",
    title="The Effects of Hours Spent Studying on the Final Score",
    labels={"Study Hours": "Hours Studied per Week", "Final Score": "Final Exam Score"},
    hover_data=["Attendance"]
)

graph_html_scatter = pio.to_html(fig_scatter, full_html=False)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/Graphs")
def graphs():
    return render_template("graphs.html", graph_html=graph_html_scatter, graph_html_pie=graph_html_pie)

if __name__ == "__main__":
    app.run(debug=False)
    


