from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
        self.value = None

    def to_html(self):
        if self.tag is None:
            raise ValueError("A tag is mandatory")
        if self.children is None:
            raise ValueError("The parent is empty")
        html = ""
        for child in self.children:
            html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"