# Re-import the required modules for generating data
from random import randint, choice
from datetime import datetime, timedelta
import pandas as pd

# Define regions and sales representatives
regions = ['North', 'South', 'East', 'West']
sales_reps = ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown']

# Generate 20 rows of random data
data = []
start_date = datetime(2024, 9, 1)
for i in range(20):
    date = start_date + timedelta(days=i)
    region = choice(regions)
    sales_rep = choice(sales_reps)
    sales_data = randint(1000, 5000)
    data.append([date.strftime('%Y-%m-%d'), region, sales_rep, sales_data])

# Create DataFrame
df = pd.DataFrame(data, columns=['Date', 'Region', 'Sales Representative', 'Sales Data'])

# Save to Excel file
file_path = './sales_data.xlsx'
df.to_excel(file_path, index=False)

file_path
