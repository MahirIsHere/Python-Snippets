from bs4 import BeautifulSoup
from requests.sessions import HTTPAdapter
import urllib3
import requests

html_page = requests.get("https://stackoverflow.com/jobs")
html_image = urllib3.PoolManager()
url = "https://stackoverflow.com/jobs"
soup = BeautifulSoup(html_page.content, "html.parser")

# title of the oage
title = soup.title
print(title)
