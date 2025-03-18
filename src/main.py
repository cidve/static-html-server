from textnode import TextNode, TextType
from copystatic import copy_directory

static_path = "./static"
public_path = "./public"

def main():

    copy_directory(static_path, public_path, erase=True)


main()