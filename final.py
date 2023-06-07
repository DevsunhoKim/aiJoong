import pandas as pd
from datetime import date

# Read the Excel file
excel_file = pd.read_excel('data1.xlsx', usecols='A')

# Get the values from the desired column
file_names = excel_file.iloc[:, 0].tolist()

# Calculate the quantity of each item
tally = {}
for name in file_names:
    if name in tally:
        tally[name] += 1
    else:
        tally[name] = 1

# Create a DataFrame with the tally results
output_df = pd.DataFrame({'Item': list(tally.keys()), 'Quantity': list(tally.values())})

# Sort the DataFrame by quantity in descending order
output_df = output_df.sort_values(by='Quantity', ascending=False)

# Get the current date
today = date.today().strftime("%Y%m%d")

# Set the output file name using the current date
output_file = f"tally_results_{today}.xlsx"

# Write the results to the output file
output_df.to_excel(output_file, index=False)

print(f"Tally results have been written to {output_file}.")
