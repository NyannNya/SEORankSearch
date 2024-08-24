# SEORankSearch

**SEORankSearch** 是一個用於查詢網站在搜尋引擎中排名的工具，該工具可以根據關鍵字和網站 URL 查詢網站的排名並生成結果報告。

## 目錄
- [專案結構](#專案結構)
- [開始使用](#開始使用)
- [使用方法](#使用方法)
- [擴展功能](#擴展功能)
- [注意事項](#注意事項)
- [授權條款](#license)

## 專案結構

```bash
SEORankSearch
├── data                            # 儲存待執行的資料 CSV 文件
├── results                         # 儲存執行爬蟲後的 CSV 文件
├── main.py                         # 主程式
├── README.md                       # 專案說明文件
├── requirements.txt                # 所需的 Python 套件列表
└── search
    ├── google.py                   # Google 搜尋排名查詢的功能模組
    └── yahoo.py                    # Yahoo 搜尋排名查詢的功能模組 (可擴展)
```


## 開始使用

1. 複製此專案到本地端：

```bash
git clone https://github.com/your-repo/SEORankSearch.git
cd SEORankSearch
```

2. 安裝所需的 Python 套件：

```bash
pip install -r requirements.txt
```

## 使用方法
準備 CSV 文件，文件名為 `data/your-file.csv`，文件中每行包括關鍵字和對應的網站 URL，如下格式：

| keyword           | website                    |
|-------------------|----------------------------|
| SEO tools         | https://www.example.com    |
| python tutorials  | https://www.example.org    |


執行`main.py`後，結果將被保存到 `results` 文件夾中，格式如下：

| keyword           | website                    | google_rank |
|-------------------|----------------------------|------|
| SEO tools         | https://www.example.com    | 3    |
| Python tutorials  | https://www.example.org    | 1    |

- keyword: 關鍵字
- website: 目標網站的 URL
- google_rank : Google Search的排名

## 擴展功能
目前此專案支援 Google 搜尋引擎的網站排名查詢（實作於 search/google.py 中）。
如需添加其他搜尋引擎（如 Yahoo、Bing 等），
可在 search/ 目錄下添加相應的 Python 模組，並擴充 main.py 中的功能。

## 注意事項
若某些行的格式不正確，程式會跳過該行並顯示警告訊息。
搜尋引擎可能會對頻繁的查詢進行限制，建議控制查詢速率以避免被封鎖。