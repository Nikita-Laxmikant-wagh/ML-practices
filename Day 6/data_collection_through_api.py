import requests
import pandas as pd

# Fetching data from the API
url = "https://poetrydb.org/title/Ozymandias/lines.json"

# Make a GET request to the API
res = requests.get(url)

# Check if the request was successful
json_data = res.json()

# Access first element, then 'lines'
lines = json_data[0]["lines"]

# Convert to DataFrame
df = pd.DataFrame(lines, columns=["Poem Lines"])

print(df)

print("DataFrame created successfully!")

# Display the shape of the DataFrame
print("DataFrame shape:", df.shape)

# Display the first five rows of the DataFrame
print("DataFrame head:\n", df.head())
