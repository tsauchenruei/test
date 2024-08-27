import requests


url = 'https://script.google.com/macros/s/AKfycbwRECz8lVVhyxbQWGHM39Eo9eqQ-9qPjT7w4PysyfKWiwStya16DzZtpA0ZaFYD24YF/exec'

# 發出 POST 請求
response = requests.get(url)

# 查看回應狀態碼
print(f'Status Code: {response.status_code}')

# 查看回應內容
print(f'Response Content: {response.text}')

