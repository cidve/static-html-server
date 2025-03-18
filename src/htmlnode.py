class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag              # A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value          # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children    # A list of HTMLNode objects representing the children of this node
        self.props = props          # A dictionary of key-value pairs representing the attributes of the HTML tag. 
                                    # For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError("This method should be implemented by subclasses")
    
    def props_to_html(self):
        #  should return a string that represents the HTML attributes of the node
        if self.props is not None:
            return " " + " ".join([f'{key}="{value}"' for key, value in self.props.items()])
        return ""


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
        
    def to_html(self):
        if self.tag == "img" and self.value is None:
            self.value = ""
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if not self.tag:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        html_str = ''
        for child in self.children:
            if not isinstance(child, HTMLNode):
                raise ValueError("invalid HTML: Children must be HTMLNode objects")
            html_str += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html_str}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.value}, {self.children}, {self.props})"


if __name__ == "__main__":
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    print(parent_node.to_html())
    print("Expected:", "<div><span>child</span></div>")

    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    print(parent_node.to_html())
    print("Expected:", "<div><span><b>grandchild</b></span></div>",)