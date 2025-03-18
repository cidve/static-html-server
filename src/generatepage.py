from markdown_blocks import markdown_to_html_node
import os

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {template_path} -> {dest_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
    to_file.close()

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")

def generate_page_recursive(from_folder_path, template_path, dest_folder_path):
    for root, _, files in os.walk(from_folder_path):
        for file in files:
            if not file.endswith(".md"):
                continue
            from_path = os.path.join(root, file)
            rel_path = os.path.relpath(from_path, from_folder_path)
            dest_path = os.path.join(dest_folder_path, os.path.splitext(rel_path)[0] + ".html")
            generate_page(from_path, template_path, dest_path)
    print(f"Generated pages in {dest_folder_path}")    