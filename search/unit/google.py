from googleapiclient.discovery import build
from . import credentials, google_search_engine_id

def get_site_rank_for_keyword(keyword: str, website: str) -> int:
    service = build('customsearch', 'v1', credentials=credentials)

    for start_index in range(1, 51, 10):  # 每次檢索10個結果，最多到第50個結果
        result = service.cse().list(
            q=keyword,
            cx=google_search_engine_id,
            num=10, 
            start=start_index,
            hl='zh-TW',  # 使用繁體中文的界面
        ).execute()

        if 'items' not in result:
            print("未找到结果或发生错误。")
            return None

        for rank, item in enumerate(result['items'], start=start_index):
            if website in item['link']:
                return rank

    return None