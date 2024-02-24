import requests
import json
import os

# Replace 'username' with the GitHub username you're interested in
username = 'Scytale-exercise'

# Optional: Insert your GitHub token here for increased rate limits
token = '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'  # Leave this as an empty string if you don't want to use a token

def get_repos(username):
    """Fetches repositories for a given GitHub username"""
    url = f'https://api.github.com/users/{username}/repos'
    headers = {'Authorization': f'token {token}'} if token else {}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        save_to_file(response.json(), 'repositories.json')
        return response.json()
    else:
        print(response.json())
        print(f'Failed to fetch repositories for user {username}')
        return []

def get_pull_requests(username, repo_name, token=None):
    """Fetches all pull requests for a given repository of a user, handling pagination."""
    pull_requests = []
    url = f'https://api.github.com/repos/{username}/{repo_name}/pulls?state=all&per_page=100'
    headers = {'Authorization': f'token {token}'} if token else {}
    
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            pull_requests.extend(response.json())
            # Check if 'Link' header is present and contains a 'next' URL
            if 'next' in response.links.keys():
                url = response.links['next']['url']
            else:
                url = None  # No more pages
        else:
            print(response.json())
            print(f'Failed to fetch pull requests for {repo_name}')
            break

    return pull_requests

def save_to_file(data, filename):
    """Saves data to a JSON file in the specified directory."""
    folder_path = '/usr/src/app/files/'# Set your folder path
    os.makedirs(folder_path, exist_ok=True)  # Create the directory if it does not exist
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        print(f"Data saved to {file_path}")

def main():
    repos = get_repos(username)
    for repo in repos:
        repo_name = repo['name']
        print(f"Repository: {repo_name}")
        pull_requests = get_pull_requests(username, repo_name)
        save_to_file(pull_requests, f"{repo['id']}.json")  # Save pull requests to file

if __name__ == "__main__":
    main()
