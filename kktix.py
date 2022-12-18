import requests
from bs4 import BeautifulSoup

url = "https://kktix.com/"
re  = requests.get(url)

if re.status_code == 200:
    print(f"successfully connected to: {url}")
else:
    print(f"error while crawling: {url}")

soup = BeautifulSoup(re.text, "lxml")

class NestedObject():
    def __init__(self, initial_attrs):
        for key in initial_attrs:
            setattr(self, key, initial_attrs[key])

def kktix_crawler():
    content = []
    # data = soup.find_all("div", {"class": "event-title"})
    data = soup.find_all("li", {"class": "type-selling"})
    for index, d in enumerate(data):
        if index <5:
            title = d.a.figure.figcaption.div.div.div.div.h2.get_text()
            image = d.a.figure.img.get("src")
            href  = d.a.get("href")
            dictionary = { 'title': title, 'image': image, 'href': href }
            content.append(dictionary)
        else:
            break
    print(content)
    return content