import pandas as pd
import requests

# Fetching data from the website
url = "https://www.scrapethissite.com/pages/simple/"

# Make a GET request to the website
res = requests.get(url)

# Check if the request was successful
if res.status_code == 200:
    print(res.text)

# Save the HTML content to a file
with open("Web Scrapping/Scrapping_data.html", "w", encoding="utf-8") as f:
    f.write(res.text)

