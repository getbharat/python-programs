import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
my_projects = response.json()

print(my_projects)

for project in my_projects:
    print(f"Project {project['name']} has url {project['web_url']}\n")