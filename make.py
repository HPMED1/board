import os
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
with open(f'./{name}.html', 'w') as f:
    lines = htmlbody
    f.writelines(lines)
os.system("git add .")
os.system("git commit -m gg")
os.system("git push")