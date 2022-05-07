from bs4 import BeautifulSoup
from requests.sessions import HTTPAdapter
import urllib3
import requests

html_page = requests.get("https://stackoverflow.com/jobs")
html_image = urllib3.PoolManager()
url = "https://stackoverflow.com/jobs"
soup = BeautifulSoup(html_page.content, "html.parser")

for sidebar in soup.find_all(
    ["li", "ol", 'class_="left-sidebar--sticky-container js-sticky-leftnav']
):
    print(sidebar.string)
