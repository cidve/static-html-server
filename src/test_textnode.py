import unittest

from textnode import TextNode, TextType


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

        
if __name__ == "__main__":
    unittest.main()