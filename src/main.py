from textnode import TextNode, TextType

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    node2 = TextNode("This is a text node", TextType.ITALIC)
    print(node)
    print(node2)


main()