import requests
from bs4 import BeautifulSoup
import random
from fake_useragent import UserAgent
import re
from urllib.parse import unquote

def get_site_rank_for_keyword(keyword: str, website: str) -> int:
    print(f"正在搜尋關鍵字 '{keyword}': {website} 在 Yahoo 的排名")
    
    query = keyword.replace(" ", "+")
    url = f"https://tw.search.yahoo.com/search?p={query}"

    ua = UserAgent()
    headers = {
        "User-Agent": ua.random,
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Referer": "https://tw.search.yahoo.com/",
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status() 

    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a", href=re.compile(r"^https://r\.search\.yahoo\.com/_ylt=.*?_ylu=.*?/RU=.*"))
    
    # 排除新聞的連結
    exclude_patterns = [
        'ftw.news.yahoo.com',
        'ftw.help.yahoo.com',
        'fn.yam.com',
        'www.ctee.com'
    ]
    links = [link for link in links if not any(pattern in link.get('href', '') for pattern in exclude_patterns)]
       
    rank = 0
    for link in links:
        href = link.get("href")
        match = re.search(r'/RU=([^&]+)', href)
        if match:
            encoded_url = match.group(1)
            actual_url = unquote(encoded_url)
            rank += 1
            if website in actual_url:
                return rank
    return None

