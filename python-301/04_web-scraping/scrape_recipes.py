import requests
from bs4 import BeautifulSoup
from pprint import pprint
from pathlib import Path




def get_detailpages_from_main(url: str) -> list:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features="html.parser")
    links = soup.find_all("a")
    href_links = [link['href'] for link in links]
    return href_links

def scrape_detail_page(link: str) -> list:
    url = f"https://codingnomads.github.io/recipes/{link}"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features="html.parser")
    page_info = []  # [title, author,instructions]
    # Find title
    title = soup.find("h1", class_="title").text[::]
    page_info.append(title)
    # Find author
    author = soup.find("p", class_="author").text[3::]
    page_info.append(author)

    # Find instructions
    instructions = soup.find("div", class_="md").text
    page_info.append(instructions)
    return page_info

detail_links = get_detailpages_from_main("https://codingnomads.github.io/recipes/")
recipes = []
for link in detail_links:
    recipes.append(scrape_detail_page(link))

path_to_file = Path.home().joinpath('Documents/codingnomads/courses/python-301/04_web-scraping').joinpath('recipes.txt')
with open(path_to_file, "w") as file:
    file.write(str(recipes))

