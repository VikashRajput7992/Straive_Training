import pandas as pd
import sqlite3

df = pd.read_csv("employees.csv")

print("Original Data:")
print(df)

# 1. Increase salary of IT employees by 10%
df.loc[df['department'] == 'IT', 'salary'] *= 1.10

# 2. Standardize names to uppercase
df['name'] = df['name'].str.upper()

# 3. Add bonus = 5% of salary
df['bonus'] = df['salary'] * 0.05

print("\nTransformed Data:")
print(df)

conn = sqlite3.connect("employees.db")

df.to_sql("employees", conn, if_exists="replace", index=False)

print("\nData has been loaded into employees.db (table: employees)")

result = pd.read_sql("SELECT * FROM employees", conn)

print("\nData from DB:")
print(result)

conn.close()