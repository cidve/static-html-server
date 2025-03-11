import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        block = "This is **bolded** paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

        block = "- This is a list\n- with items"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ULIST)

        block = "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

        block = "```python\nprint('Hello, World!')\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
        
        block = "> This is a quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)
        
        block = "1. This is an ordered list\n2. with items"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.OLIST)
        
        block = "1. This is an ordered list\n3. with items"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
        
        block = "1. This is an ordered list\n2. with items\n3. and more items"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.OLIST)
        
        block = "# This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
        
        block = "####### this is a parragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
        
        block = "### This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        md_1 = "This is a diferent block\n\nThis is a new block\n\n\n but this one I don't know what will happend"
        blocks_1 = markdown_to_blocks(md_1)
        self.assertEqual(
            blocks_1,
            [
                "This is a diferent block",
                "This is a new block",
                "but this one I don't know what will happend",
            ],
        )

    def test_markdown_to_blocks_newlines_and_spaces(self):
        md = """
This is **bolded** paragraph

 

 
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    

if __name__ == "__main__":
    unittest.main()
