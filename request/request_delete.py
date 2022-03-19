from urllib import response
import requests

urls = "https://reqres.in/api/users/2"

response = requests.delete(urls)
print(response)
print(response.status_code)

assert response.status_code == 204