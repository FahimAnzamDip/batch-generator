# Author: Fahim Anzam Dip
# Date: 8th July, 2024

import pandas as pd
import os

# Define user agent (temporary for adspower issue)
user_agent = "Mozilla/5.0 (Linux; Android 14; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.71 Mobile Safari/537.36"

def process_input_file(input_file, count):
    # Define column names
    columns = ["name", "remark", "tab", "platform", "username", "password", "fakey", 
               "cookie", "proxytype", "ipchecker", "proxy", "proxyurl", "proxyid", 
               "ip", "countrycode", "regioncode", "citycode", "ua", "resolution"]

    # Read lines from input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Process lines in chunks of 10
    for i in range(0, len(lines), count):
        chunk = lines[i:i+count]

        # Create an empty DataFrame for each chunk
        df = pd.DataFrame(columns=columns)

        # Process each line in the chunk
        for line in chunk:
            # Extract proxy information
            proxy = line.strip()
            proxy_type = "http"

            # Create a dictionary to hold the data for this line
            data = {
                "proxy": proxy,
                "proxytype": proxy_type,
                "ua": user_agent
            }

            # Append the data to the DataFrame
            df = df._append(data, ignore_index=True)

        # Write the chunk to a separate Excel file
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        
        # Create output folder if it doesn't exist
        output_folder = f"{desktop}/output_adspower"

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        output_file = f"{desktop}/output_adspower/output_{i//count}.xlsx"
        write_to_excel(df, output_file)

    print(f"Data written to {i//count + 1} files.")

    return output_folder + "/"

def write_to_excel(df, output_file):
    # Write DataFrame to Excel file
    df.to_excel(output_file, index=False)

def generate_adspower(input_file, count):
    # Process input file
    output_path = process_input_file(input_file, count)
    return output_path
