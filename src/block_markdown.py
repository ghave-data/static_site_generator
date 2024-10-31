def markdown_to_blocks(markdown):
    markdown_list = markdown.split("\n\n")
    blocks = []
    for block in markdown_list:
        if block == "":
            continue
        block = block.strip
        blocks.append(block)
    return blocks