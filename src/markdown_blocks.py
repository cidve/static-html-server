from enum import Enum

def markdown_to_blocks(markdown):
    # It takes a raw Markdown string (representing a full document) as input and returns a list of "block" strings
    blocks = []
    for block in markdown.split("\n\n"):
        block = block.strip()
        if block == "":
            continue
        blocks.append(block)
    return blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def block_to_block_type(block):
    # It takes a single block of Markdown text and returns the appropriate BlockType enum value
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif block.startswith(">"):
        return BlockType.QUOTE
    elif block.startswith("- "):
        return BlockType.ULIST
    elif block.startswith("1. "):
        # Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line
        if block.count("\n") == 0:
            return BlockType.PARAGRAPH
        lines = block.split("\n")
        for i, line in enumerate(lines):
            if line == "":
                continue
            if not line.startswith(f"{i+1}. "):
                return BlockType.PARAGRAPH
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH