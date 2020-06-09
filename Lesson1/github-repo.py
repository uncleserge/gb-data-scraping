import requests

def repos_list(data):
    for item in data:
        print(f"repo_name: {item['name']}")

api_link = 'https://api.github.com'
user_name = 'uncleserge'

url = f'{api_link}/users/{user_name}/repos'

req = requests.get(url)
if req.ok:
    data = req.json()
    repos_list(data)
else:
    print(f'error {req.status_code}')