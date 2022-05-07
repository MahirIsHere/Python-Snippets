from bs4 import BeautifulSoup
from requests.sessions import HTTPAdapter
import urllib3
import requests

html_page = requests.get("https://stackoverflow.com/jobs")
html_image = urllib3.PoolManager()
url = "https://stackoverflow.com/jobs"
soup = BeautifulSoup(html_page.content, "html.parser")

# extracting header
print("header")
for head in soup.find_all(
    ["a", "div", "ol", "li", "span", "form", "input", "button", "h3", "path"],
    class_="wmx12 mx-auto d-flex ai-center h100",
):
    print("The anchor tags are :\n", head.a.text)
    print("The div tags are :\n", head.div.text)
    print("The ol tags are :\n", head.ol.text)
    print("The li tags are :\n", head.li.text)
    print("The span tags are:\n", head.span.text)
    print("The form tags are:\n", head.form.text)
    print("The input tags are:\n", head.tags)
    print("The button tags are:\n", head.button)
    print("The h3 tags are:\n", head.h3.text)
    print("The path tags are:\n", head.path.text)
# buttons
for button1 in soup.find_all(
    "a", class_="login-link s-btn s-btn__filled py8 js-gps-track"
):
    print(button1.string)
    for button2 in soup.find_all("a", class_="login-link s-btn s-btn__primary py8"):
        print(button2.string)
