import pandas as pd

def extract_all():
    """
    Extracts data from multiple sources and returns a combined DataFrame.
    
    Returns:
        pd.DataFrame: A DataFrame containing the combined data from all sources.
    """
    # Example extraction from CSV
    csv_data = pd.read_csv('data/source1.csv')
    
    # Example extraction from Excel
    excel_data = pd.read_excel('data/source2.xlsx')
    
    # Example extraction from JSON
    json_data = pd.read_json('data/source3.json')
    
    # Combine all data into a single DataFrame
    combined_data = pd.concat([csv_data, excel_data, json_data], ignore_index=True)
    
    return combined_data