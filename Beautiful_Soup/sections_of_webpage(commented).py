from bs4 import BeautifulSoup
from requests.sessions import HTTPAdapter
import urllib3
import requests

html_page = requests.get("https://stackoverflow.com/jobs")
html_image = urllib3.PoolManager()
url = "https://stackoverflow.com/jobs"
soup = BeautifulSoup(html_page.content, "html.parser")

# title of the oage
"""title = soup.title
print(title)"""

# attributes
"""titlename = soup.title.name
print(titlename)
"""
# first div
"""div = soup.div
print(div)"""

# first link
"""
tags = soup.find_all("a")[0]
"""

# all meta_content
"""
metatags = soup.find_all("meta.")
for tag in metatags:
    print(tag.string)
"""

# Text Content Body
"""print("Body: Job Lisiting ")
for textcontent in soup.find_all(["div"], class_="listResults"):
    print(textcontent.text)"""

# header
"""for header in soup.find_all('header'):
    print(header)"""

# small Nav

"""for sNav in soup.find_all("a", class_="js-gps-track s-navigation--item"):
    print(sNav)"""

# all spans
"""for spans in soup.find_all("span"):
    print(spans.string)
"""
# class
"""navbar= soup.find_all(class_="wmx12 mx-auto d-flex ai-center h100")
print(navbar)
"""
# sidebar

"""for sidebar in soup.find_all(['li',"ol",'class_="left-sidebar--sticky-container js-sticky-leftnav']):
    print(sidebar.string)
"""

# strong

"""strong =soup.find_all("strong")
for strong in strong:
    print(strong.text)"""


# all_href
"""for a in soup.find_all('a', href=True):
    print ("URL:", a['href'])
"""
# nav_bar all div
"""for navbar in soup.find_all("div", class_="wmx12 mx-auto d-flex ai-center h100"):
    print(navbar)"""


# extracting header
"""print("header")
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
        print(button2.string)"""

# all image
"""
images = []
for img in soup.find_all("img"):
    images.append(img.get("src"))
    print(images)
"""

# footer
"""for footer in soup.find_all(['ul','li','a','nav','div','h5'],class_="site-footer--col site-footer--col__visible js-footer-col"):
    print(footer.text)
"""
# form
from bs4 import BeautifulSoup
from requests.sessions import HTTPAdapter
import urllib3
import requests

html_page = requests.get("https://stackoverflow.com/jobs")
html_image = urllib3.PoolManager()
url = "https://stackoverflow.com/jobs"
soup = BeautifulSoup(html_page.content, "html.parser")

for form in soup.find_all("form"):
    print(form.text)
