import pandas as pd
import json
import os

try:
    # Read the JSON file with explicit encoding
    print("Reading JSON file...")
    with open('perfume_data_combined.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Convert to DataFrame
    print("Converting to DataFrame...")
    df = pd.DataFrame(data)
    
    # Print DataFrame info
    print(f"DataFrame shape: {df.shape}")
    print(f"DataFrame columns: {df.columns.tolist()}")
    
    # Save to Excel with explicit encoding
    print("Saving to Excel...")
    output_file = "data_combined2.xlsx"
    
    # Convert any problematic columns to string type
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str)
    
    # Save directly to Excel
    df.to_excel(output_file, index=False, engine='openpyxl')
    
    # Verify the file was created
    if os.path.exists(output_file):
        print(f"Successfully created {output_file}")
        print(f"File size: {os.path.getsize(output_file)} bytes")
    else:
        print(f"Error: {output_file} was not created")

except Exception as e:
    print(f"An error occurred: {str(e)}") 