import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        parent_node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        self.assertEqual(parent_node.to_html(),'<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_to_html_value_error1(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode(None,[LeafNode("b", "Bold text")],None)
            parent_node.to_html()
    
    def test_to_html_value_error2(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("p",None,None)
            parent_node.to_html()

if __name__ == "__main__":
    unittest.main()   