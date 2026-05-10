000777Readme.md000777


Github Autonomous Finder




import requests

def find_ai_issue_bots():
    # We use qualifiers to target 'auto-fix' tools and AI coding agents
    # 'topic:auto-fix' finds tools designed to repair code
    # 'topic:ai-agents' finds the newer autonomous bots
    queries = [
        'topic:auto-fix',
        'topic:ai-agents',
        'topic:issue-bot',
        'AI coding assistant in:description'
    ]
    
    headers = {'Accept': 'application/vnd.github.v3+json'}
    found_repos = []

    print("--- Searching for GitHub AI & Issue Fixer Bots ---\n")

    for query in queries:
        url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc"
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            items = response.json().get('items', [])
            for item in items[:5]:  # Get top 5 from each category
                repo_data = {
                    "name": item['full_name'],
                    "description": item['description'],
                    "stars": item['stargazers_count'],
                    "url": item['html_url']
                }
                if repo_data not in found_repos:
                    found_repos.append(repo_data)
        else:
            print(f"Error searching for {query}: {response.status_code}")

    # Display the results
    for repo in found_repos:
        print(f"Repo: {repo['name']} (⭐ {repo['stars']})")
        print(f"Desc: {repo['description']}")
        print(f"Link: {repo['url']}\n")

if __name__ == "__main__":
    find_ai_issue_bots()
 