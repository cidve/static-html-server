import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node3 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node, node3)
        
        node4 = TextNode("This is a text node with diferen text", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node3, node4)

        node5 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node3, node5)
        
        node6 = TextNode("This is a text node with diferen text", TextType.BOLD, url=None)
        self.assertNotEqual(node4, node6)
        self.assertNotEqual(node, node6)
        
        node7 = TextNode("This is a text node", TextType.BOLD, url=None)
        self.assertEqual(node, node7)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        representation = "TextNode(This is a text node, bold, None)"
        self.assertEqual(representation, repr(node))
        
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        representation2 = "TextNode(This is a text node, bold, https://www.google.com)"
        self.assertEqual(representation2, repr(node2))
        
        node3 = TextNode("This is a text node", TextType.TEXT)
        representation3 = "TextNode(This is a text node, text)"
        self.assertNotEqual(representation3, repr(node3))
        
        node4 = TextNode("This is a text node", TextType.BOLD, url=None)
        representation4 = "TextNode(This is a text node, bold, None)"
        self.assertEqual(representation4, repr(node4))

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
    
    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")
    
    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")   
    
    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})
    
    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "https://www.google.com", "alt": "This is an image node"})
    
    def test_invalid_text_type(self):
        with self.assertRaises(ValueError):
            node = TextNode("This is a text node", "invalid")
            text_node_to_html_node(node)
        with self.assertRaises(ValueError):
            node = TextNode("This is a text node", None)
            text_node_to_html_node(node)
        with self.assertRaises(ValueError):
            node = TextNode("This is a text node", 123)
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()