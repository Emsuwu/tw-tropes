import html

def sanitise(input_string : str) -> str:
    try:
        return html.escape(input_string)
    except:
        return None