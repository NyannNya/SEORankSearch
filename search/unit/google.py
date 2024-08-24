import requests
from bs4 import BeautifulSoup
import random
from fake_useragent import UserAgent
import re

def get_site_rank_for_keyword(keyword: str, website: str) -> int:
    query = keyword.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}&num=50"

    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Referer": "https://www.google.com/",
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    links = soup.find_all("a", href=re.compile("^/url\?q="))

    rank = 0
    for link in links:
        href = link.get("href")
        if href and href.startswith("/url?q="):
            actual_url = href.split("/url?q=")[1].split("&")[0]
            rank += 1
            if website in actual_url:
                return rank   
    return None