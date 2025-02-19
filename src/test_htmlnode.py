import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode(tag="a", value="Click me!", props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode(tag="b", value="Click")
        node3 = HTMLNode(tag="a", value="Click me!", props={"src": 'https://www.example.com/images/dinosaur.jpg', "alt": "Dinosaur"})
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com" target="_blank"')
        self.assertEqual(node2.props_to_html(), "")
        self.assertEqual(node3.props_to_html(), ' src="https://www.example.com/images/dinosaur.jpg" alt="Dinosaur"')
        self.assertNotEqual(node1.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_values(self):
        node = HTMLNode("div", "I wish I could read", )
        self.assertEqual( node.tag, "div", )
        self.assertEqual( node.value, "I wish I could read", )
        self.assertEqual( node.children, None, )
        self.assertEqual( node.props, None, )

    def test_repr(self):
        node = HTMLNode( "p", "What a strange world", None, {"class": "primary"}, )
        self.assertEqual(  node.__repr__(), "HTMLNode(p, What a strange world, None, {'class': 'primary'})", )

if __name__ == "__main__":
    unittest.main()