from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the CSV file into a Pandas DataFrame
CSV_PATH = r"C:\Users\User\Python_Project\career_change_prediction_dataset - Copy.csv"
df = pd.read_csv(CSV_PATH)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    # Analyze the dataset
    num_rows, num_columns = df.shape
    variable_definitions = {
        "Field of Study": "The area of study the individual pursued.",
        "Current Occupation": "The current job or occupation of the individual.",
        "Age": "The age of the individual.",
        "Gender": "The gender of the individual.",
        "Years of Experience": "The number of years the individual has been working.",
        "Education Level": "The highest level of education achieved.",
        "Industry Growth Rate": "The growth rate of the industry the individual works in.",
        "Job Satisfaction": "Level of satisfaction with the current job (1-10).",
        "Work-Life Balance": "Perceived work-life balance (1-10).",
        "Job Opportunities": "Number of job opportunities available in the field.",
        "Salary": "Annual income in the current job.",
        "Job Security": "Perception of job security (1-10).",
        "Career Change Interest": "Interest in changing careers (True/False).",
        "Skills Gap": "Level of skills gap (1-10).",
        "Family Influence": "Influence of family on career decisions.",
        "Mentorship Available": "Whether mentorship is available (True/False).",
        "Certifications": "Whether certifications have been acquired (True/False).",
        "Freelancing Experience": "Experience in freelancing (True/False).",
        "Geographic Mobility": "Willingness to relocate for work (True/False).",
        "Professional Networks": "Number of professional network connections.",
        "Career Change Events": "Number of career change events experienced.",
        "Technology Adoption": "Comfort level with adopting new technology.",
        "Likely to Change Occupation": "Likelihood of changing occupation (True/False)."
    }
    column_info = [
        {"name": col, "type": str(df[col].dtype), "definition": variable_definitions.get(col, "Definition not available.")}
        for col in df.columns
    ]
    return render_template(
        'about.html',
        num_rows=num_rows,
        num_columns=num_columns,
        column_info=column_info
    )

@app.route('/data', methods=['GET'])
def data():
    # Convert the entire DataFrame to HTML for rendering in the template
    table_html = df.to_html(classes='table table-striped', index=False)
    return render_template('data.html', table_html=table_html)

if __name__ == '__main__':
    app.run(debug=True)
