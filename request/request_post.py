from urllib import response
import requests
import json
import jsonpath


urls = "https://reqres.in/api/users?page=2"

body="""{
    "name": "morpheus",
    "job": "leader"
}"""
print(type(body))
request_json = json.loads(body)
# body={}
response = requests.post(urls,request_json)
print(response.content)

assert response.status_code==201
jsonpath_res = jsonpath.jsonpath(response.json(), 'name')
assert jsonpath_res[0] == 'morpheus'
