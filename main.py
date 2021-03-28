import requests
from bs4 import BeautifulSoup

url = "https://www.verywellfamily.com/top-1000-baby-girl-names-2757832"
r = requests.get(url)

soup = BeautifulSoup(r.content, features="html.parser")

ol = soup.find("ol", {"id": "mntl-sc-block_1-0-13"})

names = [li.text for li in ol.findAll("li")][:10]
names.sort()

print(names)
