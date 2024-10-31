import re

def extract_markdown_images(text):
    matches_names = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches_names

def extract_markdown_links(text):
    matches_names = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches_names