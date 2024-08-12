import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://www.appclick.ng") 

soup = BeautifulSoup(response.content, "html.parser")

header = soup.find("header")

logo = header.find("div", attrs={
    'class': "logo"
})

logo_image = logo.find("img", attrs={'class': 'logo-light'})

print(logo_image.attrs['src'])

# print(soup.prettify())

print(soup.find_all("div"))


file = open("div.txt", "w")

file.write(str(soup.find_all("div")))

file.close()