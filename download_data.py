"""
Download the Telecom Customer Churn dataset
This script fetches the data from a public source and saves it locally
"""

import requests
import os

# Create data directory if it doesn't exist
os.makedirs('data/raw', exist_ok=True)

# Download URL for the Telco Churn dataset
# (Public source from GitHub)
url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-demo/master/data/WA_Fn-UseC_.csv"

print("📥 Downloading telecom churn dataset...")
print(f"From: {url}")

try:
    # Download the file
    response = requests.get(url)
    response.raise_for_status()  # Check if download was successful
    
    # Save to the correct location
    filepath = 'data/raw/WA_Fn-UseC_.csv'
    with open(filepath, 'w') as f:
        f.write(response.text)
    
    print(f"✅ Success! Data saved to: {filepath}")
    
except Exception as e:
    print(f"❌ Error downloading: {e}")
    print("Try downloading manually from: https://www.kaggle.com/datasets/blastchar/telco-customer-churn")

