import requests
from bs4 import BeautifulSoup

url = "https://ticket.ibon.com.tw/Index/entertainment"
re  = requests.get(url)

if re.status_code == 200:
    print(f"successfully connected to: {url}")
else:
    print(f"error while crawling: {url}")

soup = BeautifulSoup(re.text, "lxml")

def ibon_crawler():
    content = []
    data = soup.find_all("div", {"class": "owl-item"})
    for index, d in enumerate(data):
        if index <5:
            title = d.div.a.get("title")
            image = d.div.a.figure.img.get("src")
            href  = d.div.a.get("href")
            dictionary = { 'title': title, 'image': image, 'href': "https://ticket.ibon.com.tw"+href }
            content.append(dictionary)
        else:
            break
    print(content)
    return content