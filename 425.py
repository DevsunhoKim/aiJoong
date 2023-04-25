import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel('data1.xlsx')

# Split each item by spaces and count the frequency of complete items and substrings
freq = {}
for item in df.iloc[:,0]:
    # Check for the existence of multi-word items before splitting by spaces
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
        # Check for the existence of multi-word items after splitting by spaces
        if "보기드문 사진들" in item:
            substring = "보기드문 사진들"
            if substring not in freq:
                freq[substring] = 1
            else:
                freq[substring] += 1
        elif "rare photos" in item:
            substring = "rare photos"
            if substring not in freq:
                freq[substring] = 1
            else:
                freq[substring] += 1

# Print the frequency for each complete item and substring
for substring, count in freq.items():
    print(substring, count)
