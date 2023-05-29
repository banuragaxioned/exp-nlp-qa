from bs4 import BeautifulSoup
from markdown import markdown

def markdown_to_text(markdown_string):
    """ Converts a markdown string to plaintext """
  
    # md -> html -> text since BeautifulSoup can extract text cleanly
    html = markdown(markdown_string)
  
    # remove code snippets
    soup = BeautifulSoup(html, "html.parser")
    for code in soup("code"):
        code.decompose()
    
    # extract text
    text = ''.join(soup.stripped_strings)
  
    return text

markdown_text = """
# Header
This is a paragraph with **bold text**.

Here is a list:
- Item 1
- Item 2

And here is some code: `print("Hello, World!")`
"""

plain_text = markdown_to_text(markdown_text)

print(plain_text)
