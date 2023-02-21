import requests

url = "https://api.github.com/users/frotaadriano/repos"

response = requests.get(url)

if response.status_code == 200:
    repos = response.json()
    for repo in repos:
        print(f"Language: {repo['language']}")
        print(f"URL: {repo['html_url']}")
        print(f"Description: {repo['description']}")
        print("-" * 50)
else:
    print("Failed to retrieve repository data")
