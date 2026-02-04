import html

def sanitise(input_string : str) -> str:
    return html.escape(input_string)

test = "nyehe im evil <script>killWebsite()</script>"
print(sanitise(test))