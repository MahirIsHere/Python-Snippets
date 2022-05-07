from bs4 import BeautifulSoup
from requests.sessions import HTTPAdapter
import urllib3
import requests

html_page = requests.get("https://stackoverflow.com/jobs")
html_image = urllib3.PoolManager()
url = "https://stackoverflow.com/jobs"
soup = BeautifulSoup(html_page.content, "html.parser")
# nav_bar all div
for navbar in soup.find_all("div", class_="wmx12 mx-auto d-flex ai-center h100"):
    print(navbar)
