import requests
import logging
import time
from datetime import datetime
# 設置日誌處理器
file_handler = logging.FileHandler('log.txt')

# 創建 root_logger
root_logger = logging.getLogger()
root_logger.addHandler(file_handler)
root_logger.setLevel(logging.DEBUG)
ggg = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
# 記錄一條信息
root_logger.info(f'Hi!{ggg}')

# 要發送 POST 請求的 URL
url = 'https://stock.tsau.us.kg/post-text-test'
#url = 'http://127.0.0.1:5000/post'

# 要發送的資料
data = {"text": "test"}

# 發出 POST 請求
response = requests.post(url, data=data)

# 查看回應狀態碼
print(f'Status Code: {response.status_code}')

# 查看回應內容
print(f'Response Content: {response.text}')

# 記錄回應的狀態碼和內容
root_logger.debug(f"{response.status_code} {response.text}")
