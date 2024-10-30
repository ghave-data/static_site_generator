import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        node = HTMLNode("div", "This is a test")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "This is a test")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
    def test_to_html(self):
        node = HTMLNode(props = {
        "href": "https://www.google.com", 
        "target": "_blank",
        }
        )
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode(tag="p", value="test value")
        self.assertEqual(repr(node), 'HTMLNode(p, test value, None, None)')


if __name__ == "__main__":
    unittest.main()