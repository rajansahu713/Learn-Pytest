from cgitb import reset
import requests
import json
import jsonpath

urls = "https://reqres.in/api/users?page=2"

response = requests.get(urls)
#print(response.content)

json_respose = json.loads(response.text)

#print(json_respose)


page=jsonpath.jsonpath(json_respose, 'total_pages')
print(page[0])

assert page[0] == 5