import requests
import json
import jsonpath


urls="https://reqres.in/api/users/2"

body = """{
    "name": "morpheus",
    "job": "zion resident"
}"""
response = requests.put(urls, json.loads(body))

jsonpath_res = jsonpath.jsonpath(response.json(), 'name') 

assert response.status_code == 200
print(response.content)