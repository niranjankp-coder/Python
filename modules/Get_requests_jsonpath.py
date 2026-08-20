import requests
import jsonpath

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

json_data = response.json()

for x in range(0,5):
    result = jsonpath.jsonpath(json_data, f"$.[{x}].title")
    print(f"THE TITLE OF ID IS: {result}")
