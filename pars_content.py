import requests
from bs4 import BeautifulSoup as bs


url = "https://www.nytimes.com/" # Your site, example - https://www.nytimes.com/




def pars(url):
    lst = list(url)
    part = lst[8:-1]
    x = ("".join(part))
    r = requests.get(url)
    sp = bs(r.text, "html.parser")
    with open("data2.txt", "w", encoding="utf-8") as f:
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if url[0] == "/":
                f.write("\n" + x + url)
            if "html" in url:
                f.write("\n" + url)


pars(url)
