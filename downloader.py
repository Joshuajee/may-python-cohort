import requests


url = "https://www.appclick.ng/assets/img/hero/appclick-academy-courses-top-notch-IT-consulting-company-in-ibadan-lagos-nigeria.jpg"
# Send a GET request to the website
response = requests.get(url)

if response.status_code == 200:
    image = open("image.jpg", "wb")
    print(response.content)
    image.write(response.content)
    image.close()
else:
    print(response.status_code)