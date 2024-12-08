from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

# Paths
CSV_PATH = os.path.join(os.path.dirname(__file__), "career_change_prediction_dataset.csv")
DB_PATH = os.path.join(os.path.dirname(__file__), "career_database.db")

# Debug file existence
assert os.path.exists(CSV_PATH), f"File not found: {CSV_PATH}"
assert os.path.exists(DB_PATH), f"Database file not found: {DB_PATH}"

# Load the dataset
df = pd.read_csv(CSV_PATH)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    num_rows, num_columns = df.shape
    variable_definitions = {
        # Add column definitions here
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
    table_html = df.to_html(classes='table table-striped', index=False)
    return render_template('data.html', table_html=table_html)

if __name__ == '__main__':
    app.run(debug=True)
