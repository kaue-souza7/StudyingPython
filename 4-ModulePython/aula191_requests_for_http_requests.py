# requests para requisições HTTP
import requests

# http:// -> 80
# https:// -> 443

url = 'http://localhost:3330/'
response = requests.get(url)

print(response.headers)
print(response.content)
print(response.text)

