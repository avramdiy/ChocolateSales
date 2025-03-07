from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__, template_folder=r'C:\Users\Ev\Desktop\TRG Week 14\templates')

# Path to your CSV file
csv_file_path = r"C:\Users\Ev\Desktop\TRG Week 14\Chocolate Sales.csv"

# Load data into a Pandas DataFrame
def load_data():
    try:
        df = pd.read_csv(csv_file_path)
        return df
    except Exception as e:
        return f"Error loading data: {e}"

@app.route('/')
def display_data():
    data = load_data()

    if isinstance(data, str):  # If an error occurred
        return data

    # Convert the DataFrame to an HTML table
    table_html = data.to_html(classes='table table-bordered', index=False)

    return render_template('data.html', table_html=table_html)

if __name__ == '__main__':
    app.run(debug=True)
