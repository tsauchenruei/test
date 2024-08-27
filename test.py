import requests
import logging
import time
from datetime import datetime


# 要發送 POST 請求的 URL
url = 'https://stock.tsau.us.kg/post-text-test'
#url = 'http://127.0.0.1:5000/post'

# 要發送的資料
data = {"text": "1223"}

# 發出 POST 請求
response = requests.post(url, data=data)

# 查看回應狀態碼
print(f'Status Code: {response.status_code}')

# 查看回應內容
print(f'Response Content: {response.text}')



url = 'https://script.google.com/macros/s/AKfycbwRECz8lVVhyxbQWGHM39Eo9eqQ-9qPjT7w4PysyfKWiwStya16DzZtpA0ZaFYD24YF/exec'

# 發出 POST 請求
response = requests.get(url)

# 查看回應狀態碼
print(f'Status Code: {response.status_code}')

# 查看回應內容
print(f'Response Content: {response.text}')

