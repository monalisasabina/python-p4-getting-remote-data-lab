import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)
    

results= GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json').get_response_body()   
print(results)

results_json = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json').load_json()
print(results_json)
print(json.dumps(results_json,indent = 1))