from bs4 import BeautifulSoup
 
with open("Web Scrapping/Scrapping_data.html","r") as f:
    html_content=f.read()

soup = BeautifulSoup(html_content,"lxml")
print(soup)

#display first h1 tag 
all_h1_tags = soup.find_all("h1")
print(all_h1_tags)

#display all h3 tags
all_h3_tags = soup.find_all("h3")
print(all_h3_tags)

#display all the text in the html page
print(soup.get_text())

#display all the text in the html page without spaces
all_contries=[]
for h3 in all_h3_tags:
    names = h3.get_text(strip=True)
    population = h3.find_next("div").select("span.country-population")[0].get_text(strip=True)
    print(h3.find_next("div").select_one("span.country-population").get_text(strip=True))
    all_contries.append([names,population])

# Display the list of all countries and their population
print(all_contries)

# Convert the list of countries and their population to a DataFrame
import pandas as pd
df = pd.DataFrame(all_contries,columns=["Country","Population"])
print(df)

# Save the DataFrame to a CSV file
df.to_csv("Web Scrapping/countries_population.csv",index=False)