import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_values(self):
        leaf_node = LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(leaf_node.tag, "a")
        self.assertEqual(leaf_node.value, "Click me!")
        self.assertEqual(leaf_node.children, None)
        self.assertEqual(leaf_node.props, {"href": "https://www.google.com"})

    def test_to_html1(self):
        leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf_node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_to_html2(self):
        leaf_node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf_node.to_html(), '<p>This is a paragraph of text.</p>')

    def test_to_html3(self):
        with self.assertRaises(ValueError):
            leaf_node = LeafNode("p", None)
            leaf_node.to_html()

    def test_to_html4(self):
        leaf_node = LeafNode(None, "No tag")
        self.assertEqual(leaf_node.to_html(), "No tag")



if __name__ == "__main__":
    unittest.main()
