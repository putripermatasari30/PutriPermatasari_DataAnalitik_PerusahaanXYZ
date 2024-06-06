Inventory Data Analysis
This project analyzes inventory data using Python. The analysis includes data loading, data cleaning, data visualization, correlation analysis, and linear regression modeling. The following steps are detailed in this README:

Data Collection
Data Cleaning
Data Visualization
Correlation Analysis
Linear Regression Modeling
Model Evaluation
Data Description
The inventory data is stored in a CSV file named inventory_data.csv. The file contains the following columns:

ItemID: Unique identifier for each item.
ItemName: Name of the item.
Category: Category to which the item belongs.
Stock: Number of items available in stock.
Price: Price of the item.
ReorderLevel: Stock level at which the item should be reordered.
Sample data:

csv
Copy code
ItemID,ItemName,Category,Stock,Price,ReorderLevel
1,Item A,Category 1,50,20,10
2,Item B,Category 2,30,15,5
3,Item C,Category 1,70,25,20
4,Item D,Category 2,20,10,5
5,Item E,Category 3,60,30,15
6,Item F,Category 3,10,50,10
7,Item G,Category 1,40,20,10
8,Item H,Category 2,25,15,5
9,Item I,Category 3,55,35,15
10,Item J,Category 1,65,20,20
Code Explanation
The analysis is implemented in Python and includes the following steps:

1. Data Collection
The data is read from the CSV file using the pandas library.

python
Copy code
import pandas as pd

data = pd.read_csv('inventory_data.csv')
2. Data Cleaning
Basic information about the data is displayed, including the first few rows, data types, missing values, and descriptive statistics.

python
Copy code
print("Lima baris pertama data:")
print(data.head())

print("\nInformasi umum tentang data:")
print(data.info())

print("\nRingkasan statistik tentang data:")
print(data.describe())

print("\nJumlah data yang hilang dalam setiap kolom:")
print(data.isnull().sum())

print("\nJumlah nilai unik dalam setiap kolom:")
print(data.nunique())

print("\nTipe data dari setiap kolom:")
print(data.dtypes)
3. Data Visualization
Several visualizations are created to explore the data:

Scatter Plot of Stock vs Price
Histogram of Price
Box Plot of Stock
Bar Plot of Categories
python
Copy code
import matplotlib.pyplot as plt

# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(data['Stock'], data['Price'], color='blue', alpha=0.5)
plt.title('Scatter Plot of Stock vs Price')
plt.xlabel('Stock')
plt.ylabel('Price')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(data['Price'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Price')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Box Plot
plt.figure(figsize=(10, 6))
plt.boxplot(data['Stock'].dropna())
plt.title('Box Plot of Stock')
plt.ylabel('Stock')
plt.show()

# Bar Plot of Categories
category_data = data['Category'].unique()
count_data = data['Category'].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(category_data, count_data, color=['blue', 'green', 'orange'])
plt.title('Barplot of Categories')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()
4. Correlation Analysis
The correlation between numerical variables is calculated and visualized using a heatmap.

python
Copy code
import seaborn as sns

correlation = data.corr()
print("\nKorelasi antara variabel:")
print(correlation)

plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation')
plt.show()
5. Linear Regression Modeling
A linear regression model is created to predict the price based on stock levels.

python
Copy code
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

X = data[['Stock']]
y = data['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Prediksi
y_pred = model.predict(X_test)
6. Model Evaluation
The model is evaluated using the Mean Squared Error (MSE) metric and the results are visualized.

python
Copy code
mse = mean_squared_error(y_test, y_pred)
print("\nMean Squared Error (MSE):", mse)

plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('Stock')
plt.ylabel('Price')
plt.title('Actual vs Predicted Price')
plt.legend()
plt.show()
Running the Analysis
Ensure you have Python installed (preferably Python 3.7 or later).
Install the necessary libraries:
bash
Copy code
pip install pandas matplotlib seaborn scikit-learn
Save the inventory_data.csv file in the same directory as your script.
Run the inventory_analysis.py script:
bash
Copy code
python inventory_analysis.py
Conclusion
This project demonstrates how to perform basic data analysis, visualization, and linear regression modeling on inventory data. The results provide insights into the relationships between stock levels and prices, and help in making informed decisions about inventory management.

