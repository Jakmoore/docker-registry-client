import requests
from requests.api import get

BASE_URL = "http://127.0.0.1:5000/v2/"

def main() -> None:
    catalog_response = requests.get(f"{BASE_URL}/_catalog")
    repos = catalog_response.json().get("repositories")
    repos_and_tags = {}

    for repo in repos:
        name = repo.split("/connect-adapters/")[1]
        tags_response = requests.get(f"{BASE_URL}/{name}/tags/list")
        latest = tags_response.json().get("tags")[0].split(",")[-1]
        repos_and_tags[name] = latest

    print_to_console(repos_and_tags)

def print_to_console(repos_and_tags):
    max_key_len = max(map(len, repos_and_tags.keys()))
    format_string = '{{key:{}}}  {{value}}'.format(max_key_len)

    for key, value in repos_and_tags.items():
        print(format_string.format(key=key, value=value))

if __name__ == "__main__":
    main()