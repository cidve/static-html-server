import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node1 = LeafNode("p", "Hello, world!", props={"class": "primary"})
        self.assertEqual(node1.to_html(), '<p class="primary">Hello, world!</p>')
        node2 = LeafNode("p", "Hello, world!", {"class": "primary", "id": "main"})
        self.assertEqual(node2.to_html(), '<p class="primary" id="main">Hello, world!</p>')
        node3 = LeafNode("p", "Hello, world!", {"class": "primary", "id": "main", "style": "color: red;"})
        self.assertNotEqual(node3.to_html(), '<p class="primary" id="main">Hello, world!</p>')
        self.assertEqual(node3.to_html(), '<p class="primary" id="main" style="color: red;">Hello, world!</p>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        print(parent_node.to_html())
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",)
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()