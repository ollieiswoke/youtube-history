import urllib.request
from bs4 import BeautifulSoup
def title_from_url(url):
    page = urllib.request.urlopen(url)
    html = BeautifulSoup(page.read(), "html.parser")
    title = html.title.string[:-10]
    return title

