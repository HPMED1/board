import os
import console
ifreame = input()
htmlbody = (f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="msapplication-TileImage" content="./prof.png">
    <meta property="og:site_name" content="HPMED's board">
    <meta property="og:title" content="I think i got something funny for you">
    <meta property="og:image" itemprop="image" content="./prof.png">
    <meta property="og:type" content="website" />
    <meta property="og:image:type" content="image/png">
    <meta property="og:image:width" content="300">
    <meta property="og:image:height" content="300">
    <title>HPMED's board</title>
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
console.print_step(f"https://hpmed1.github.io/board/{name}")