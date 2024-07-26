import requests
# pip install requests 로 설치하면 global에 설치됨

url = 'https://random-data-api.com/api/v2/users'
response = requests.get(url).json()

print(response)
