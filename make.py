import os
from github import Github
ifreame = input()
htmlbody = (f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <center>
    {ifreame}
    </center>
</body>
</html>
""")
name=input()
from github import Github

# First, create a Github instance:
g = Github("YOUR_GITHUB_ACCESS_TOKEN")

# Next, get the repository that you want to update:
repo = g.get_repo("USERNAME/REPO_NAME")

# Then, get the contents of the file that you want to update:
file = repo.get_contents("FILE_PATH")

# Update the contents of the file:
repo.update_file(file.path, "Updated content", "New commit message", file.sha)

# Finally, push the changes back to GitHub:
repo.push()

with open(f'./share/{name}.html', 'w') as f:
    lines = htmlbody
    f.writelines(lines)
