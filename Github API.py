from github import Github
g = Github("e210816fcfe6db157e77b168fa83ddb4c7a7272c")
for repo in g.get_user().get_repos():
    print(repo.name)