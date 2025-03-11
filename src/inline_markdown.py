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

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0],TextType.IMAGE,image[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


if __name__ == '__main__':
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    node = TextNode(text, TextType.TEXT)
    print(split_nodes_image([node]))

    # text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # extract_markdown_links(text)
    # node = TextNode(text, TextType.TEXT)
    # print(split_nodes_link([node]))
    # # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]