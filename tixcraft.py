import requests
from bs4 import BeautifulSoup

url = "https://tixcraft.com/"
re  = requests.get(url)

if re.status_code == 200:
    print(f"successfully connected to: {url}")
else:
    print(f"error while crawling: {url}")

soup = BeautifulSoup(re.text, "lxml")

def tixcraft_crawler():
    content = []
    data = soup.find_all("div", {"class": "col-md-4 col-sm-6 col-xs-12"})
    for index, d in enumerate(data):
        if index <5:
            title = d.div.a.img.get("alt")
            image = d.div.a.img.get("src")
            href  = d.div.a.get("href")
            dictionary = { 'title': title, 'image': image, 'href': "https://tixcraft.com"+href }
            content.append(dictionary)
        else:
            break
    print(content)
    return content