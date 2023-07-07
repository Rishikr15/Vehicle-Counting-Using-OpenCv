from bs4 import BeautifulSoup
with open("scrap.html","r") as f:
    doc = BeautifulSoup(f, 'html.parser')

tag = doc.find_all("head")[0]
tag.string = "New Title"
print(tag)