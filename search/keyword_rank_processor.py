import os
import csv
from typing import Optional
from search.unit.google import get_site_rank_for_keyword

class KeywordRankProcessor:
    def __init__(self, input_directory: str, output_directory: str) -> None:
        """
        初始化 KeywordRankProcessor 物件。

        :param input_directory: 輸入 CSV 檔案所在的資料夾路徑。
        :param output_directory: 輸出結果 CSV 檔案要儲存的資料夾路徑。
        """
        self.input_directory = input_directory
        self.output_directory = output_directory
    
    def process_keywords_and_websites(self, input_file: str, output_file: str) -> None:
        """
        讀取指定的 CSV 檔案，取得關鍵字和網站的排名，並將結果寫入輸出檔案。

        :param input_file: 輸入 CSV 檔案的路徑。
        :param output_file: 輸出結果 CSV 檔案的路徑。
        """
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            
            # 寫入標題行
            writer.writerow(['keyword', 'website', 'rank'])
            next(reader, None)
            
            for row in reader:
                if len(row) >= 2:
                    keyword: str = row[0]
                    website: str = row[1]
                    rank: Optional[int] = get_site_rank_for_keyword(keyword, website)
                    if rank == -1:
                        rank = None
                    writer.writerow([keyword, website, rank])
                else:
                    print(f"警告：行 {row} 格式不正確，已跳過")
    
    def process_all_csv_in_directory(self) -> None:
        """
        處理輸入目錄中的所有 CSV 檔案，並將結果儲存到輸出目錄中，維持原檔名。

        :return: None
        """
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)
        
        for filename in os.listdir(self.input_directory):
            if filename.endswith('.csv'):
                input_file: str = os.path.join(self.input_directory, filename)
                output_file: str = os.path.join(self.output_directory, filename)
                self.process_keywords_and_websites(input_file, output_file)
                print(f"處理完成 {filename}。結果已保存到 {output_file}")