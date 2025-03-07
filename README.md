# TRG Week 14 Project

## Chocolate Sales Data Analysis

- Link to Dataset : https://www.kaggle.com/datasets/atharvasoundankar/chocolate-sales

### 1st Commit

- Created data.py, README.md, app & templates folders.

- Loaded data to the ('/') route to see beginning data.

### 2nd Commit

- Clean data. Remove "Sales Person" attribute.
- Print all individual values within "Product" attribute and clean.
- Rename all occurrences of "Choco" to Choc.
- Rename all occurrences of "Bar" to Choc.
- Rename all occurrences of "Organic Choc Syrup" to Liquid Choc.
- Rename all occurrences of "Drinking Coco" to Liquid Choc.
- Rename all occurrences of "Choc Coated Almonds" to Almond Choc.
- Rename all occurrences of "Peanut Butter Cubes" to PB Choc.
- Rename all occurrences of "85% Dark Choc" to Dark Choc.
- Rename all occurrences of "50% Dark Bites" to Dark Choc.
- Rename all occurrences of "Mint Choc Chip" to Mint Choc.
- Rename all occurrences of "Smooth Sliky Salty" to Milk Choc.
- Rename all occurrences of "99% Dark & Pure" to Dark Choc.
- Rename all occurrences of "After Nines" to Mint Choc.
- Rename all occurrences of "Eclairs" to Milk Choc.
- Rename all occurrences of "Spicy Special Slims" to Spicy Choc.
- Rename all occurrences of "Fruit & Nut Choc" to FruitNut Choc.
- Rename all occurrences of "Manuka Honey Choc" to Honey Choc.
- Rename all occurrences of "Baker's Choc Chips" to Choc Chips.
- Rename all occurrences of "Caramel Stuffed Choc" to Caramel Choc.
- Rename all occurrences of "70% Dark Bites" to Dark Choc.

- All data is ready for analysis.

### 3rd Commit

- I want to visualize a pie chart showing the combined amount sold of all types of choc, for all countries.

- Create pie_chart.html

- Convert "Amount" values into integers from string.

- After visualizing, I can see Dark, Milk, Liquid, Mint, Almond Choc are the top 5 sold, in their respective order.

- Also fixed "Choc Chip" to be "Chip Choc" for analysis.

### 4th Commit

- I want to visualize a bar chart for USA under the "Country" column. I want all choc types on the X axis, and the total Amount sold per type, on the Y axis.

- Created ('/usa-bar-chart') route.

- Created bar_chart.html.

### 5th Commit

- I want to visualize a line plot. I want to aggregate the total monthy amount sold by country. I want the Y axis to be the "Amount", and the X axis will represent the months. I want each line a different color to represent each country in the dataset, with a legend for viewers.

- Created line_plot.html.

- Created ('/line-plot') route.

- I can see that the UK has times where chocolate cravings peak in Jan and June.

- I can also tell that Canada has a pretty low average consumption of chocolate.

- A further analysis could give us the moving average of the best chocolates to sell in which months, or which countries prefer which chocolates at certain times.

- Nice project. On to Week 15 then.