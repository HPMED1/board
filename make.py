import os
import console
iframe = input("iframe/site: ")
if iframe.startswith("<"):
    iframe=iframe
else:
    iframe = f'<iframe src="{iframe}">'
embed = input("embed: ")
htmlbody = (f"""<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="icon" type="image/png" href="share.png">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta property="og:site_name" content="HPMED's board">
    <meta property="og:title" content="I think i got something funny for you">
    <title>HPMED's board</title>
    </head>
<style>
    body {{
      background-color: #2c2f33;
    }}
    h1{{
        color: white;
    }}
  </style>
<body>
    <center>
    <h1>Welcome to my board, where I share shit that I think is funny</h1>
    {iframe}
    {embed}
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
console.print_step(f"https://hpmed1.github.io/board/{name}")