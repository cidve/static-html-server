from textnode import TextNode, TextType
from copystatic import copy_directory
import os
import shutil
from generatepage import generate_page

# Directories
static_path = "./static"
public_path = "./public"

# Information
markdown_path = "./content/index.md"
template_path = "./template.html"
html_path = "./public/index.html"


def main():
    if os.path.exists(public_path):
        print(f"Deleting {public_path}...")
        shutil.rmtree(public_path)
    copy_directory(static_path, public_path)
    generate_page(markdown_path, template_path, html_path)

main()