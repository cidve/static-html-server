from textnode import TextNode, TextType
def main():
    text_node = TextNode("Hello", TextType.NORMAL_TEXT, url="www.boot.dev")
    print(text_node)

main()