#  Web Scraper for News Headlines
""" Hints/Mini Guide:
 1.Use requests to fetch HTML
 2.Use BeautifulSoup to parse <h2> or title tags
 3.Save the titles in a .txt file"""

import requests
from bs4 import BeautifulSoup

url = "https://indianexpress.com/"
response = requests.get(url)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("h2")
    with open("headlines.txt", "w", encoding="utf-8") as file:
        file.write("Top News Headlines:\n")

        for i, h in enumerate(headlines):
            text = h.get_text().strip()
            if text: 
                print(f"{i+1}. {text}")
                file.write(f"{i+1}. {text}\n")

    print("\n Headlines have been saved to 'headlines.txt'")

else:
    print("Please valid News webpage :", response.status_code)

