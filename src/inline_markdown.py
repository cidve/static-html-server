from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # It takes a list of "old nodes", a delimiter, and a text type. It should return a new list of nodes, 
    # where any "text" type nodes in the input list are (potentially) split into multiple nodes based on the syntax.
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
            continue
        elif node.text_type == TextType.TEXT:
            text = node.text
            if text.count(delimiter) % 2 != 0:
                raise ValueError("Invalid Markdown syntax: Delimiter count is not even")
            split_nodes = []
            sections = text.split(delimiter)
            for i in range(len(sections)):
                if sections[i] == "":
                    continue
                if i % 2 == 0:
                    split_nodes.append(TextNode(sections[i], TextType.TEXT))
                else:
                    split_nodes.append(TextNode(sections[i], text_type))

            nodes.extend(split_nodes)
    return nodes

def extract_markdown_images(text):
    # takes raw markdown text and returns a list of tuples.
    # Each tuple should contain the alt text and the URL of any markdown images.
    # If there are no images, return an empty list.
    pattern = re.compile(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)")
    return pattern.findall(text)

def extract_markdown_links(text):
    # extracts markdown links instead of images. It should return tuples of anchor text and URLs
    pattern = re.compile(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)")
    return pattern.findall(text)


if __name__ == '__main__':
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))

    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))
    # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]