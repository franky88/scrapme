from bs4 import BeautifulSoup
from requests_html import HTMLSession
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

s = HTMLSession()
# url = "https://www.rebelgunworks.com.au/collections/all-rifles"

def getURL(url):
    r = s.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    return soup

def getPages(soup):
    page = soup.find("ul", class_="pagination-custom")
    # link = page.find_all("li")
    # for a in link:
    #     print(a.find("a")["href"])
    # return link
    if not page.find("li", class_="disabled", string="→"):
        url = "https://www.rebelgunworks.com.au" + str(page.find("li", string="→").find("a")['href'])
        return url
    else:
        return
# data = []
# while True:
#     soup = getURL(url)
#     url = getPages(soup)
#     data.append(url)
#     if not url:
#         break
#     # df = pd.read_excel(data)
#     print(data)

@app.route('/', methods=['GET'])
def getelementdata():
    r = s.get("https://python.org")
    url = "https://www.rebelgunworks.com.au/collections/all-rifles"
    # soup = getPages(url)
    data = []
    while True:
        soup = getURL(url)
        url = getPages(soup)
        data.append(url)
        if not url:
            break
    print(url)
    return render_template("index.html", req=url)