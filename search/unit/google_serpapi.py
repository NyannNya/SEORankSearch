from serpapi import search
from . import serpapi_key

# 輸入你的 API 金鑰
api_key = serpapi_key

def get_site_rank_for_keyword(query: str, site: str) -> int:
    # 設定搜尋參數
    params = {
        'q': query,
        'num': 100,  # 設定每頁的搜尋結果數量
        'api_key': api_key
    }

    rank = 0

    # 初始化 GoogleSearch 類別
    google_search = search(params)
    results = google_search.as_dict()

    # 檢查搜尋結果
    for result in results.get('organic_results', []):
        rank += 1
        link = result.get('link')
        if site in link:
            return rank

    return None