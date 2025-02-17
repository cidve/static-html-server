from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text    # The text content of the node
        self.text_type = text_type  #The type of text this node contains, which is a member of the TextType enum.
        self.url = url  #The URL of the link or image, if the text is a link. Default to None if nothing is passed in.
    
    def __eq__(self, text_node):
        return (self.text == text_node.text
                and self.text_type == text_node.text_type
                and self.url == text_node.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"