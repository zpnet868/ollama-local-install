import requests
API_URL = "http://localhost:11434/api/generate"
headers = {
    "Content-Type": "application/json"
}
data = {
    "model": "deepseek-r1:1.5b",  # 填写模型名称
    "prompt": "你好",
    "stream": False
}
response = requests.post(API_URL, headers=headers, json=data)
if response.status_code == 200:
    result = response.json()
    print(result["response"])