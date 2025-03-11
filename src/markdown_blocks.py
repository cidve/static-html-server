
def markdown_to_blocks(markdown):
    # It takes a raw Markdown string (representing a full document) as input and returns a list of "block" strings
    blocks = []
    for block in markdown.split("\n\n"):
        block = block.strip()
        if block == "":
            continue
        blocks.append(block)
    return blocks