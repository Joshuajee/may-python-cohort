import requests
from bs4 import BeautifulSoup


url = "https://www.tvcnews.tv/"

response = requests.get(url) 

soup = BeautifulSoup(response.content, "html.parser")

print(soup)

# testimonail_div = soup.find("div", attrs={"class" : "testimonial-slider-one"})

# testimonails = testimonail_div.find_all("div", attrs={"class": "testimonial-item"})

# output = []

# for testimonail in testimonails:
#     image = testimonail.find("img")
#     image_src = image.attrs['src']
#     name = testimonail.find("h5")
#     reviews = testimonail.find("p")
  
#     output.append([url, name.text, image_src, reviews.text])
#     #print(testimonail)
    


# df = pd.DataFrame(output, columns=["Website", "Fullname", "Image", "Reviews"])

# df.to_csv("testimonial3.csv", index_label="S/N")
# print(questions)


# file = open("output.txt", "w")

# file.write(text)

# file.close()
