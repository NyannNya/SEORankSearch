from search.keyword_rank_processor import KeywordRankProcessor

input_directory = 'data'
output_directory = 'results'

# 建立資料夾路徑
processor = KeywordRankProcessor(input_directory, output_directory)

# 執行所有 CSV 檔案的處理
processor.process_all_csv_in_directory()

print(f"所有檔案處理完成。結果已保存到 {output_directory}")
