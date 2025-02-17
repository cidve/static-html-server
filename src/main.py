from textnode import TextNode, TextType
def main():
    text_node = TextNode("Hello", TextType.BOLD, url="www.boot.dev")
    print(text_node)

main()