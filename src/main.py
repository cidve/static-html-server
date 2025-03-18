from textnode import TextNode, TextType
from copystatic import copy_directory
import os
import shutil
from generatepage import generate_page_recursive

# Directories
static_path = "./static"
public_path = "./public"

# Information
markdown_folder_path = "./content/"
template_path = "./template.html"
html_folder_path = "./public/"


def main():
    if os.path.exists(public_path):
        print(f"Deleting {public_path}...")
        shutil.rmtree(public_path)
    copy_directory(static_path, public_path)
    generate_page_recursive(markdown_folder_path, template_path, html_folder_path)

main()