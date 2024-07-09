# Author: Fahim Anzam Dip
# Date: 8th July, 2024

import pandas as pd
import os

def process_input_file(input_file, count):
    # Define column names
    columns = ["Profile name", "Cookie", "Proxy type", "Proxy", "User Agent", "Notes"]

    # Read lines from input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Profile name counter
    profile_name_counter = 1

    # Process lines in chunks of count
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
                "Profile name": profile_name_counter,
                "Proxy": proxy,
                "Proxy type": proxy_type
            }

            # Append the data to the DataFrame
            df = df._append(data, ignore_index=True)

            # Increment the profile name counter
            profile_name_counter += 1

        # Write the chunk to a separate Excel file
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        
        # Create output folder if it doesn't exist
        output_folder = f"{desktop}/output_dolphin"

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        output_file = f"{desktop}/output_dolphin/output_{i//count}.xlsx"
        write_to_excel(df, output_file)

    print(f"Data written to {i//count + 1} files.")

    return output_folder + "/"

def write_to_excel(df, output_file):
    # Write DataFrame to Excel file
    df.to_excel(output_file, index=False)

def generate_dolphin(input_file, count):
    # Process input file
    output_path = process_input_file(input_file, count)
    return output_path

