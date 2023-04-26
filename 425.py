import pandas as pd
import datetime

# Read the Excel file named 'data1.xlsx' into a DataFrame.
df = pd.read_excel('data1.xlsx')

# Iterate through each row of the DataFrame, splitting the row into individual items and counting the frequency of each item.
freq = {}
for item in df.iloc[:,0]:
    # Convert the dict that stores item frequencies to a DataFrame and sort by frequency in descending order.
    # Exceptions are made for items that contain spaces.
    if "눈부시게 아름다운 사진들" in item:
        substring = "눈부시게 아름다운 사진들"
        if substring not in freq:
            freq[substring] = 1
        else:
            freq[substring] += 1
    else:
        substrings = item.split()
        for i in range(len(substrings)):
            substring = ' '.join(substrings[:i+1])
            if substring not in freq:
                freq[substring] = 1
            else:
                freq[substring] += 1
    
        if "보기드문 사진들" in item:
            substring = "보기드문 사진들"
            if substring not in freq:
                freq[substring] = 1
            else:
                freq[substring] += 1

# Create a DataFrame from the frequency dictionary and sort by frequency in descending order.
df_freq = pd.DataFrame(freq.items(), columns=['substring', 'count']).sort_values(by=['count'], ascending=False)

# Generate file name with current date.
file_name = datetime.datetime.now().strftime("%Y-%m-%d") + '.csv'

# Write the DataFrame to a CSV file with the current date as the file name, specifying encoding and delimiter.
df_freq.to_csv(file_name, index=False, encoding='utf-8', sep=',')

# Print the frequency count for each item.
for substring, count in freq.items():
    print(substring, count)
