import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# read excel file
df = pd.read_excel('data.xlsx', engine='openpyxl')

# Normalize text in all columns
df = df.apply(lambda x: x.str.lower().str.strip() if x.dtype == "object" else x)

# Write the updated data to a new Excel file
df.to_excel('output_file.xlsx', index=False)

# group by item and sum quantities
item_counts = df.groupby('item')['quantity'].sum()

# output the shipment quantity for each item
for item, count in item_counts.items():
    print(f'{item}: {count}')


# Read the normalized data from an Excel file
df = pd.read_excel('output_file.xlsx')

# Extract the item names
items = df['item'].tolist()

# Vectorize the item names using the TF-IDF algorithm
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(items)

# Cluster the items using the k-means algorithm
kmeans = KMeans(n_clusters=5, random_state=0).fit(X)

# Print the cluster labels for each item
labels = kmeans.labels_
for i, item in enumerate(items):
    print(f'{item}: {labels[i]}')    


    # 파이썬 실행 파일화
