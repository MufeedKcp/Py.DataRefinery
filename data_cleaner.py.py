import pandas as pd
import numpy as np

input_file = "data/customers_raw.csv"
output_file = "data/cleaned_data.csv"

try:
    df = pd.read_csv(input_file)
except Exception as e:
        print(f'ERROR: {e}')

def transformation(customer_data):
    customer_data['name'] = customer_data['name'].str.strip().str.lower()
    customer_data['email'] = customer_data['email'].str.strip().str.lower()
    df['email'] = df['email'].replace(r'^\s*$', np.nan, regex=True)
    customer_data['country'] = customer_data['country'].str.lower()
    customer_data['age'] = pd.to_numeric(customer_data['age'], errors='coerce').astype('Int64')
    customer_data['signup_date'] = pd.to_datetime(customer_data['signup_date'])
    cleaned_df = df.dropna(subset=['email'])
    return cleaned_df.drop_duplicates()


if __name__ == '__main__':
    print('custoemr data cleaning started......')
    cleaned_data = transformation(df)
    print('Done! Data is now cleaned')
else:
    print(f"Skipping transformation: not extracted.")
    
cleaned_data.to_csv(output_file, index=False, sep='\t')
