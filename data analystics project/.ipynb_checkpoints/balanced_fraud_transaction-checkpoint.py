import pandas as pd
import numpy as np

# Define the columns for the dataset
columns = [
    "Transaction_ID", "User_ID", "Transaction_Amount", "Transaction_Date", 
    "Transaction_Time", "Merchant_Name", "Merchant_Location", "Payment_Method", 
    "Transaction_Status", "Fraud_Flag", "User_Account_Balance", "User_Device_Type", 
    "User_Transaction_History_Count", "User_Age", "User_Gender", "User_Country", 
    "Transaction_Type", "Merchant_Category", "User_Account_Status"
]

# Generate synthetic data
np.random.seed(42)
data = {
    "Transaction_ID": [f"TID{1000+i}" for i in range(2000)],
    "User_ID": [f"UID{np.random.randint(1000, 2000)}" for _ in range(2000)],
    "Transaction_Amount": np.round(np.random.uniform(10, 5000, 2000), 2),
    "Transaction_Date": pd.date_range(start="2024-01-01", periods=2000, freq="H").date,
    "Transaction_Time": pd.date_range(start="2024-01-01", periods=2000, freq="H").time,
    "Merchant_Name": [f"Merchant_{np.random.randint(1, 100)}" for _ in range(2000)],
    "Merchant_Location": [f"Location_{np.random.randint(1, 50)}" for _ in range(2000)],
    "Payment_Method": np.random.choice(["UPI", "Credit Card", "Debit Card", "Net Banking"], 2000),
    "Transaction_Status": np.random.choice(["Success", "Failed", "Pending"], 2000),
    # Create a balanced Fraud_Flag
    "Fraud_Flag": np.concatenate([np.ones(1000, dtype=int), np.zeros(1000, dtype=int)]),
    "User_Account_Balance": np.round(np.random.uniform(1000, 100000, 2000), 2),
    "User_Device_Type": np.random.choice(["Android", "iOS"], 2000),
    "User_Transaction_History_Count": np.random.randint(1, 500, 2000),
    "User_Age": np.random.randint(18, 70, 2000),
    "User_Gender": np.random.choice(["Male", "Female", "Other"], 2000),
    "User_Country": np.random.choice(["India", "USA", "UK", "Germany", "Australia", "Canada"], 2000),
    "Transaction_Type": np.random.choice(["Purchase", "Transfer", "Withdrawal", "Deposit"], 2000),
    "Merchant_Category": np.random.choice(["Grocery", "Electronics", "Fashion", "Healthcare", "Travel"], 2000),
    "User_Account_Status": np.random.choice(["Active", "Inactive", "Suspended"], 2000)
}

# Shuffle the data to mix fraudulent and non-fraudulent transactions
df = pd.DataFrame(data).sample(frac=1).reset_index(drop=True)

# Save to CSV
file_path = "gpay_fraud_transaction_analysis_balanced.csv"
df.to_csv(file_path, index=False)

print(f"Balanced dataset saved to {file_path}")
