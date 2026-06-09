import pandas as pd
# Load dataset
df = pd.read_csv("Global_Superstore.csv/Global Superstore.csv")
print("=" * 50)
print("DATA CLEANING AND PREPARATION")
print("=" * 50)
print("\nOriginal Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nTotal Missing Values:", df.isnull().sum().sum())
print("\nDuplicate Rows:", df.duplicated().sum())
# Handle missing values
df = df.dropna()
# Remove duplicates
df = df.drop_duplicates()
# Convert date column
if "Order Date" in df.columns:
    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    print("\nOrder Date converted to datetime format.")
print("\nData Types:")
print(df.dtypes)
print("\nCleaned Shape:", df.shape)
# Export cleaned data
df.to_csv("Cleaned_Global_Superstore.csv", index=False)
print("\nCleaned dataset exported successfully!")
print("Output File: Cleaned_Global_Superstore.csv")