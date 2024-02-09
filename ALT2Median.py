import csv
import pandas
import statistics

# Read the entire CSV file into a pandas DataFrame
df = pandas.read_csv('screentimeALT2.csv')
print("df to string")
print(df.to_string())

# Filter out the column, value_eur
daily_values = df['Daily average screentime (decimal)']
weekly_values = df['Screentime (Weekly)(Decimal)']
print("Daily average screentime (decimal) values",type(daily_values),daily_values)

# Find daily median
median_value_daily = round(daily_values.median(), 2)
print("Median Value Daily average screentime (decimal):", median_value_daily)

#Find weekly median
median_value_weekly = round(weekly_values.median(), 2)
print("Median Value Screentime (Weekly)(Decimal):", median_value_weekly)



