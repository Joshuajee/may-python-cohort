import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.appclick.ng") 

soup = BeautifulSoup(response.content, "html.parser")

faq_div = soup.find("div", attrs={"id" : "accordionExample"})

print(faq_div.find_all("h3"))

faqs = faq_div.find_all("div", attrs={"class": "accordion-item"})

questions = []
text = ""
for faq in faqs:
    question = faq.find("button", attrs={"class": "accordion-button collapsed"})
    answer = faq.find("p")
    questions.append({"quesion": question.text, "answer": answer.text})
    print(question.text)
    print(answer.text)
    
    text += question.text.strip() + "\n" + answer.text.strip() + "\n\n\n"
    
    
print(questions)


file = open("output.txt", "w")

file.write(text)

file.close()
