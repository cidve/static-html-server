import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node

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

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and _more_ items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

if __name__ == "__main__":
    unittest.main()
