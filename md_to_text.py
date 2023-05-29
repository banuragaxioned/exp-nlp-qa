import os
from bs4 import BeautifulSoup
from markdown import markdown

def markdown_to_text(md_file_path, output_dir):
    """ Reads a markdown file and converts it to plaintext """
  
    # Read markdown file
    with open(md_file_path, 'r') as f:
        markdown_string = f.read()

    # md -> html -> text since BeautifulSoup can extract text cleanly
    html = markdown(markdown_string)

    # remove code snippets
    soup = BeautifulSoup(html, "html.parser")
    for code in soup("code"):
        code.decompose()
    
    # extract text
    text = ''.join(soup.stripped_strings)
  
    # Write to output file
    output_file_path = os.path.join(output_dir, os.path.basename(md_file_path) + '.txt')
    with open(output_file_path, 'w') as f:
        f.write(text)

def convert_all_markdown(input_dir, output_dir):
    """ Convert all markdown files in a directory (and its subdirectories) to plaintext """

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".md"):
                markdown_to_text(os.path.join(root, file), output_dir)


convert_all_markdown('./data/raw/', './data/processed')
