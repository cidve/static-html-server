import os
import shutil
import sys
from generatepage import generate_pages_recursive
from copystatic import copy_directory

# Directories
static_path = "./static"
public_path = "./public"
dir_path_public = "./docs"

# Information
markdown_folder_path = "./content/"
template_path = "./template.html"
html_folder_path = "./public/"
default_basepath = "static-html-server/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    if os.path.exists(public_path):
        print(f"Deleting {public_path}...")
        shutil.rmtree(public_path)
    copy_directory(static_path, dir_path_public)
    generate_pages_recursive(markdown_folder_path, template_path, dir_path_public, basepath)

main()