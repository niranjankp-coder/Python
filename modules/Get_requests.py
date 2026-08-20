import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
print(response.content)
print(response.headers)
print(response.status_code)
print(response.json())
