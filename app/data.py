from flask import Flask, render_template, send_from_directory, Response
import pandas as pd
import matplotlib.pyplot as plt
import os
import io

app = Flask(__name__, template_folder=r'C:\Users\Ev\Desktop\TRG Week 14\templates')

# Path to your CSV file
csv_file_path = r"C:\Users\Ev\Desktop\TRG Week 14\Chocolate Sales.csv"

# Load data into a Pandas DataFrame
def load_data():
    try:
        df = pd.read_csv(csv_file_path)
        if "Sales Person" in df.columns:
            df = df.drop(columns=["Sales Person"])
        return df
    except Exception as e:
        return f"Error loading data: {e}"

@app.route('/')
def display_data():
    data = load_data()

    if isinstance(data, str):  # If an error occurred
        return data

    # Replace all occurrences of 'Choco' with 'Choc' in the "Product" column
    if "Product" in data.columns:
        data["Product"] = data["Product"].str.replace("Choco", "Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Bars", "Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Organic Choc Syrup", "Liquid Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Drinking Coco", "Liquid Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Choc Coated Almonds", "Almond Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Peanut Butter Cubes", "PB Choc", regex=False)
        data["Product"] = data["Product"].str.replace("85% Dark Choc", "Dark Choc", regex=False)
        data["Product"] = data["Product"].str.replace("50% Dark Bites", "Dark Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Mint Chip Choc", "Mint Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Smooth Sliky Salty", "Milk Choc", regex=False)
        data["Product"] = data["Product"].str.replace("99% Dark & Pure", "Dark Choc", regex=False)
        data["Product"] = data["Product"].str.replace("After Nines", "Mint Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Eclairs", "Milk Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Spicy Special Slims", "Spicy Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Fruit & Nut Choc", "FruitNut Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Manuka Honey Choc", "Honey Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Baker's Choc Chips", "Chip Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Caramel Stuffed Choc", "Caramel Choc", regex=False)
        data["Product"] = data["Product"].str.replace("70% Dark Bites", "Dark Choc", regex=False)
        product_values = data["Product"].unique().tolist()
        # Print the unique product values after replacement
        print(product_values)
    else:
        product_values = []

    # Convert the DataFrame to an HTML table
    table_html = data.to_html(classes='table table-bordered', index=False)

    return render_template('data.html', table_html=table_html, product_values=product_values)

@app.route('/pie-chart')
def pie_chart():
    data = load_data()

    if isinstance(data, str):  # If an error occurred
        return data

    # Ensure "Amount" column exists
    if "Amount" not in data.columns:
        return "Error: 'Amount' column not found in the dataset."
    
    # Clean the "Amount" column by removing non-numeric characters (like $ and commas)
    data["Amount"] = data["Amount"].replace({r'[^\d.]': ''}, regex=True)

    # Convert "Amount" to numeric values (this will convert any invalid values to NaN)
    data["Amount"] = pd.to_numeric(data["Amount"], errors='coerce')

    # Replace all occurrences of 'Choco' with 'Choc' in the "Product" column
    if "Product" in data.columns:
        data["Product"] = data["Product"].str.replace("Choco", "Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Bars", "Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Organic Choc Syrup", "Liquid Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Drinking Coco", "Liquid Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Choc Coated Almonds", "Almond Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Peanut Butter Cubes", "PB Choc", regex=False)
        data["Product"] = data["Product"].str.replace("85% Dark Choc", "Dark Choc", regex=False)
        data["Product"] = data["Product"].str.replace("50% Dark Bites", "Dark Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Mint Chip Choc", "Mint Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Smooth Sliky Salty", "Milk Choc", regex=False)
        data["Product"] = data["Product"].str.replace("99% Dark & Pure", "Dark Choc", regex=False)
        data["Product"] = data["Product"].str.replace("After Nines", "Mint Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Eclairs", "Milk Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Spicy Special Slims", "Spicy Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Fruit & Nut Choc", "FruitNut Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Manuka Honey Choc", "Honey Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Baker's Choc Chips", "Chip Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Caramel Stuffed Choc", "Caramel Choc", regex=False)
        data["Product"] = data["Product"].str.replace("70% Dark Bites", "Dark Choc", regex=False)
        product_values = data["Product"].unique().tolist()
        # Print the unique product values after replacement
        print(product_values)
    else:
        product_values = []

    # Filter rows where "Product" contains "Choc"
    choc_data = data[data["Product"].str.contains("Choc", case=False, na=False)]

    # Group by "Product" and sum the sales
    choc_sales = choc_data.groupby("Product")["Amount"].sum()

    # Plotting the pie chart
    fig, ax = plt.subplots()
    ax.pie(choc_sales, labels=choc_sales.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.

    # Save the plot to a BytesIO object (in-memory image)
    img_io = io.BytesIO()
    plt.savefig(img_io, format='png')
    img_io.seek(0)
    plt.close()

    # Return the pie chart image as a response
    return Response(img_io, mimetype='image/png')

@app.route('/usa-bar-chart')
def bar_chart():
    data = load_data()

    if isinstance(data, str):  # If an error occurred
        return data

    # Ensure "Amount" and "Country" columns exist
    if "Amount" not in data.columns or "Country" not in data.columns:
        return "Error: 'Amount' or 'Country' column not found in the dataset."
    
    # Clean the "Amount" column by removing non-numeric characters (like $ and commas)
    data["Amount"] = data["Amount"].replace({r'[^\d.]': ''}, regex=True)

    # Convert "Amount" to numeric values (this will convert any invalid values to NaN)
    data["Amount"] = pd.to_numeric(data["Amount"], errors='coerce')
    
    # Replace all occurrences of 'Choco' with 'Choc' in the "Product" column
    if "Product" in data.columns:
        data["Product"] = data["Product"].str.replace("Choco", "Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Bars", "Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Organic Choc Syrup", "Liquid Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Drinking Coco", "Liquid Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Choc Coated Almonds", "Almond Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Peanut Butter Cubes", "PB Choc", regex=False)
        data["Product"] = data["Product"].str.replace("85% Dark Choc", "Dark Choc", regex=False)
        data["Product"] = data["Product"].str.replace("50% Dark Bites", "Dark Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Mint Chip Choc", "Mint Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Smooth Sliky Salty", "Milk Choc", regex=False)
        data["Product"] = data["Product"].str.replace("99% Dark & Pure", "Dark Choc", regex=False)
        data["Product"] = data["Product"].str.replace("After Nines", "Mint Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Eclairs", "Milk Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Spicy Special Slims", "Spicy Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Fruit & Nut Choc", "FruitNut Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Manuka Honey Choc", "Honey Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Baker's Choc Chips", "Chip Choc", regex=False)
        data["Product"] = data["Product"].str.replace("Caramel Stuffed Choc", "Caramel Choc", regex=False)
        data["Product"] = data["Product"].str.replace("70% Dark Bites", "Dark Choc", regex=False)
        product_values = data["Product"].unique().tolist()
        # Print the unique product values after replacement
        print(product_values)
    else:
        product_values = []

    # Filter the data to include only rows where the country is 'USA'
    usa_data = data[data["Country"] == "USA"]

    # Group by "Product" and sum the "Amount" sold for each product in the USA
    choc_sales_usa = usa_data.groupby("Product")["Amount"].sum()

    # Plotting the bar chart
    fig, ax = plt.subplots()
    choc_sales_usa.plot(kind='bar', ax=ax)
    ax.set_xlabel('Chocolate Type')
    ax.set_ylabel('Total Amount Sold')
    ax.set_title('Total Chocolate Sales by Type (USA)')

    # Save the plot to a BytesIO object (in-memory image)
    img_io = io.BytesIO()
    plt.savefig(img_io, format='png')
    img_io.seek(0)
    plt.close()

    # Return the bar chart image as a response
    return Response(img_io, mimetype='image/png')

@app.route('/line-plot')
def line_plot():
    data = load_data()

    if isinstance(data, str):  # If an error occurred
        return data

    # Ensure "Amount", "Country", and "Date" columns exist
    if "Amount" not in data.columns or "Country" not in data.columns or "Date" not in data.columns:
        return "Error: 'Amount', 'Country', or 'Date' column not found in the dataset."
    
    # Clean the "Amount" column by removing non-numeric characters (like $ and commas)
    data["Amount"] = data["Amount"].replace({r'[^\d.]': ''}, regex=True)

    # Convert "Amount" to numeric values (this will convert any invalid values to NaN)
    data["Amount"] = pd.to_numeric(data["Amount"], errors='coerce')

    # Convert the "Date" column to datetime
    data["Date"] = pd.to_datetime(data["Date"], errors='coerce')

    # Extract the Year-Month from the "Date" column
    data["Year-Month"] = data["Date"].dt.to_period('M')

    # Group by "Country" and "Year-Month" and sum the "Amount"
    monthly_sales = data.groupby(["Country", "Year-Month"])["Amount"].sum().unstack(fill_value=0)

    # Plotting the line plot with "Year-Month" on the X-axis
    fig, ax = plt.subplots(figsize=(10, 6))
    monthly_sales.T.plot(kind='line', ax=ax, marker='o')  # Transpose the DataFrame to get months on X-axis

    ax.set_xlabel('Month')
    ax.set_ylabel('Total Amount Sold')
    ax.set_title('Total Monthly Sales by Country')
    ax.legend(title='Country')

    # Save the plot to a BytesIO object (in-memory image)
    img_io = io.BytesIO()
    plt.savefig(img_io, format='png')
    img_io.seek(0)
    plt.close()

    # Return the line plot image as a response
    return Response(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
