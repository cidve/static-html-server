import unittest
from inline_markdown import (
    split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
)
from textnode import TextNode, TextType

class TestInlineMarkdown(unittest.TestCase):

    def text_split_nodes_delimiter_bold(self):
        text_nodes = [
            TextNode("This is a text node", TextType.TEXT),
            TextNode("**This is a bold node**", TextType.TEXT),
            TextNode("This is a text node", TextType.TEXT),
            TextNode("**This is a bold node**", TextType.TEXT),
        ]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(text_nodes, delimiter, text_type)
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text, "This is a text node")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "This is a bold node")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, "This is a text node")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "This is a bold node")
        self.assertEqual(new_nodes[3].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[4].text, "This is a text node")

    def text_split_nodes_delimiter_text_in_between(self):
        text_nodes = [TextNode('**hola** mi nombre es **gabriel**, ahora **probando entremedio** del texto', TextType.TEXT),
                        TextNode('ahora _probando_ _entremedio_ del texto', TextType.TEXT)]
        delimiter = "**"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(text_nodes, delimiter, text_type)
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text, "hola")
        self.assertEqual(new_nodes[0].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[1].text, " mi nombre es ")
        self.assertEqual(new_nodes[1].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, "gabriel")
        self.assertEqual(new_nodes[2].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[3].text, ", ahora ")
        self.assertEqual(new_nodes[3].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[4].text, "probando entremedio")
        self.assertEqual(new_nodes[4].text_type, TextType.BOLD)

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        matches_1 = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image", "https://i.imgur.com/zjjcJKZ.png")], matches_1)

    def test_extract_markdowns_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)
        matches_1 = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches_1)
    
    def test_extract_markdowns_links_and_images(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and ![image](https://.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)
        matches_1 = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches_1)


    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another link", TextType.LINK, "https://blog.boot.dev"),
                TextNode(" with text that follows", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 10)
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "text")
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text, " with an ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "italic")
        self.assertEqual(nodes[3].text_type, TextType.ITALIC)
        self.assertEqual(nodes[4].text, " word and a ")
        self.assertEqual(nodes[4].text_type, TextType.TEXT)
        self.assertEqual(nodes[5].text, "code block")
        self.assertEqual(nodes[5].text_type, TextType.CODE)
        self.assertEqual(nodes[6].text, " and an ")
        self.assertEqual(nodes[6].text_type, TextType.TEXT)
        self.assertEqual(nodes[7].text, "obi wan image")
        self.assertEqual(nodes[7].text_type, TextType.IMAGE)
        self.assertEqual(nodes[8].text, " and a ")
        self.assertEqual(nodes[8].text_type, TextType.TEXT)
        self.assertEqual(nodes[9].text, "link")
        self.assertEqual(nodes[9].text_type, TextType.LINK)
        self.assertEqual(nodes[9].url, "https://boot.dev")
        
        text_1 = "This text contains nothing special"
        nodes_1 = text_to_textnodes(text_1)
        self.assertEqual(len(nodes_1), 1)
        self.assertEqual(nodes_1[0].text, "This text contains nothing special")
        self.assertEqual(nodes_1[0].text_type, TextType.TEXT)
        
        text_2 = "This text contains nothing _special_ I lied has **Itatic** and _bold_"
        nodes_2 = text_to_textnodes(text_2)
        self.assertEqual(len(nodes_2), 6)
        self.assertEqual(nodes_2[0].text, "This text contains nothing ")
        self.assertEqual(nodes_2[0].text_type, TextType.TEXT)
        self.assertEqual(nodes_2[1].text, "special")
        self.assertEqual(nodes_2[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes_2[2].text, " I lied has ")
        self.assertEqual(nodes_2[2].text_type, TextType.TEXT)
        self.assertEqual(nodes_2[3].text, "Itatic")
        self.assertEqual(nodes_2[3].text_type, TextType.BOLD)
        self.assertEqual(nodes_2[4].text, " and ")
        self.assertEqual(nodes_2[4].text_type, TextType.TEXT)
        self.assertEqual(nodes_2[5].text, "bold")
        self.assertEqual(nodes_2[5].text_type, TextType.ITALIC)
    
    def test_text_to_textnodes_errors(self):
        text_3 = "this ones has an **error"
        with self.assertRaises(ValueError):
            text_to_textnodes(text_3)

        text_4 = "this ones has an _error"
        with self.assertRaises(ValueError):
            text_to_textnodes(text_4)

if __name__ == "__main__":
    unittest.main()
