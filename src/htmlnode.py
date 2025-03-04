

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
        if not self.value:
            raise ValueError("invalid HTML: no value")
        if not self.tag:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


if __name__ == "__main__":
    test_1 = HTMLNode(tag="a", value="Click me!", props={"href": "https://www.google.com", "target": "_blank"})
    # print(test_1.to_html())  # <a href="https://www.google.com" target="_blank">Click me!</a>
    print(str(test_1))  # HTMLNode(a, Click me!, None, {'href': 'https://www.google.com', 'target': '_blank'})
    print(test_1.props_to_html())  # href="https://www.google.com" target="_blank"