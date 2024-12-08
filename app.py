from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

# Paths
DATASET_PATH = os.path.join(os.path.dirname(__file__), "career_change_prediction_dataset.csv")

# Verify file existence
assert os.path.exists(DATASET_PATH), f"File not found: {DATASET_PATH}"

# Load the dataset
df = pd.read_csv(DATASET_PATH)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data')
def data():
    table_html = df.to_html(classes='data-table', index=False)
    return render_template('data.html', table_html=table_html)

@app.route('/about')
def about():
    # Dataset variable definitions
    variable_definitions = [
        {"name": "Field of Study", "type": "object", "definition": "Area of study pursued by the individual."},
        {"name": "Current Occupation", "type": "object", "definition": "The current job or role held by the individual."},
        {"name": "Age", "type": "int64", "definition": "The individual's age."},
        {"name": "Gender", "type": "object", "definition": "The individual's gender."},
        {"name": "Years of Experience", "type": "int64", "definition": "Total years of work experience."},
        {"name": "Education Level", "type": "object", "definition": "The highest educational qualification achieved."},
        {"name": "Industry Growth Rate", "type": "object", "definition": "Growth rate of the industry the individual works in."},
        {"name": "Job Satisfaction", "type": "int64", "definition": "Level of satisfaction with the current job (1-10)."},
        {"name": "Work-Life Balance", "type": "int64", "definition": "Perceived work-life balance (1-10)."},
        {"name": "Job Opportunities", "type": "int64", "definition": "Number of job opportunities available in the field."},
        {"name": "Salary", "type": "int64", "definition": "Annual income in the current job."},
        {"name": "Job Security", "type": "int64", "definition": "Perception of job security (1-10)."},
        {"name": "Career Change Interest", "type": "bool", "definition": "Interest in changing careers."},
        {"name": "Skills Gap", "type": "int64", "definition": "Level of skills gap (1-10)."},
        {"name": "Family Influence", "type": "object", "definition": "Influence of family on career decisions."},
        {"name": "Mentorship Available", "type": "bool", "definition": "Whether mentorship is available."},
        {"name": "Certifications", "type": "bool", "definition": "Whether certifications have been acquired."},
        {"name": "Freelancing Experience", "type": "bool", "definition": "Experience in freelancing."},
        {"name": "Geographic Mobility", "type": "bool", "definition": "Willingness to relocate for work."},
        {"name": "Professional Networks", "type": "int64", "definition": "Number of professional network connections."},
        {"name": "Career Change Events", "type": "int64", "definition": "Number of career change events experienced."},
        {"name": "Technology Adoption", "type": "int64", "definition": "Comfort level with adopting new technology."},
        {"name": "Likely to Change Occupation", "type": "bool", "definition": "Likelihood of changing occupation."},
    ]
    return render_template('about.html', variables=variable_definitions, num_rows=df.shape[0], num_columns=df.shape[1])

if __name__ == "__main__":
    app.run(debug=True)
