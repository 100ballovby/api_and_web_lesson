import requests as r

url = 'https://www.onliner.by'
response = r.get(url)

print(response.status_code)
