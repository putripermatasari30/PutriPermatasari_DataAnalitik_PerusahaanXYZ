import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Membaca file data
data = pd.read_csv('inventory.csv')

# Menampilkan lima baris pertama data
print("Lima baris pertama data:")
print(data.head())

# Menampilkan informasi umum tentang data
print("\nInformasi umum tentang data:")
print(data.info())

# Menampilkan ringkasan statistik tentang data numerik
print("\nRingkasan statistik tentang data:")
print(data.describe())

# Menampilkan jumlah data yang hilang (missing values) dalam setiap kolom
print("\nJumlah data yang hilang dalam setiap kolom:")
print(data.isnull().sum())

# Menampilkan jumlah unik dari setiap nilai dalam suatu kolom
print("\nJumlah nilai unik dalam setiap kolom:")
print(data.nunique())

# Menampilkan tipe data dari setiap kolom
print("\nTipe data dari setiap kolom:")
print(data.dtypes)

# Visualisasi Data
# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(data['Quantity'], data['UnitPrice'], color='blue', alpha=0.5)
plt.title('Scatter Plot of Quantity vs Unit Price')
plt.xlabel('Quantity')
plt.ylabel('Unit Price')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(data['Quantity'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Quantity')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.show()

# Box Plot
plt.figure(figsize=(10, 6))
plt.boxplot(data['Quantity'].dropna())
plt.title('Box Plot of Quantity')
plt.ylabel('Quantity')
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

# Analisis Korelasi
correlation = data[['Quantity', 'UnitPrice']].corr()
print("\nKorelasi antara variabel:")
print(correlation)

# Heatmap Korelasi
plt.figure(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation')
plt.show()

# Pemodelan Regresi Linier
X = data[['Quantity']]
y = data['UnitPrice']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Prediksi
y_pred = model.predict(X_test)

# Evaluasi Model
mse = mean_squared_error(y_test, y_pred)
print("\nMean Squared Error (MSE):", mse)

# Visualisasi Hasil Prediksi
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('Quantity')
plt.ylabel('Unit Price')
plt.title('Actual vs Predicted Unit Price')
plt.legend()
plt.show()
