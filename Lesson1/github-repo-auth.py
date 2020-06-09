import requests

def repos_list(data):
    for item in data:
        repo_type = ('public', 'private')[item['private']]
        print(f"repo_name: {item['name']} _{repo_type}")


api_link = 'https://api.github.com'
token = 'a27af870100a05e47d831c2de446cac4962b2172'

url = f'{api_link}/user/repos?access_token={token}'

req = requests.get(url)
if req.ok:
    data = req.json()
    repos_list(data)
else:
    print(f'error {req.status_code}')