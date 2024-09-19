# github_api_funcs.py

from github import Github

def get_repo_info(repo_name, token):
    g = Github(token)
    repo = g.get_repo(repo_name)
    return {
        "name": repo.name,
        "description": repo.description,
        "url": repo.html_url
    }

# Add more functions as needed
