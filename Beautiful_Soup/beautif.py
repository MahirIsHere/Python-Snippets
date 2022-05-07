from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://stackoverflow.com/jobs").text
soup = BeautifulSoup(html_text, "lxml")

print(soup.prettify())
