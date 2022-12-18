import requests
from bs4 import BeautifulSoup

url = "https://tw.news.yahoo.com/search?p=%E6%BC%94%E5%94%B1%E6%9C%83&fr=news&fr2=p%3Anews%2Cm%3Asb"
re  = requests.get(url)

if re.status_code == 200:
    print(f"successfully connected to: {url}")
else:
    print(f"error while crawling: {url}")

soup = BeautifulSoup(re.text, "lxml")

def news_crawler():
    content = ""

    data = soup.find_all("h3", {"class": "Mb(5px)"})
    for index, d in enumerate(data):
            if index <5:
                title = d.a.text
                href  = d.a.get("href")
                content += "{}\n{}\n".format(title, "https://tw.news.yahoo.com/"+href)
            else:
                break
    print(content)
    return content