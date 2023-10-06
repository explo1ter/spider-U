import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pyfiglet

print("\n"+"*"*65)
print(pyfiglet.figlet_format("          SPIDER-U"))
print("*\t\t\tBy Nibil Mathew\t\t\t\t*")
print("*\t\t\tgithub:explo1ter\t\t\t*")
print("\n"+"*"*65)

visited_urls = set()
def spider_url(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f"Request failed {url}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get('href')
            if href is not None and href != "":
                urls.append(href)
    for url2 in urls:
        if url2 not in visited_urls:
            visited_urls.add(url2)
            url_join = urljoin(url, url2)
            if keyword in url_join:
                print(url_join)
                spider_url(url_join, keyword)

url = input("Enter the url to spider(complete url required) : ")
keyword = input("Enter the keyword : ")
spider_url(url, keyword)
