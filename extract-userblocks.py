from bs4 import BeautifulSoup
import os
import shutil
# Create the base folder layout for jeckyll
# -----------------------------------------

# folders = ["_includes", "_data", "_layouts", "_posts", "_templates", "_templates/contentblocks", "pages"]

# for folder in folders:
#     if not os.path.exists(folder):
#         os.makedirs(folder)

# Correct the paths
# -----------------

with open("index.html", "r") as f:
    contents = f.read()

modified_contents = contents.replace("assets/", "/assets/")

with open("index.html", "w") as f:
    f.write(modified_contents)


# Extract scripts-block

# Set the path to the HTML file
html_file = "index.html"

# Set the path to the output file
output_file = os.path.join("_includes", "scripts.html")

# Open the HTML file and read its contents
with open(html_file) as f:
    html = f.read()

# Create a BeautifulSoup object and find all the <script> tags within the <body> section
soup = BeautifulSoup(html, 'html.parser')
scripts = soup.body.find_all('script')

# Remove the <script> tags from the original HTML file
for script in scripts:
    script.extract()

# Write the modified HTML to the original file
with open(html_file, "w") as f:
    f.write(str(soup))

# Write the <script> tags to the output file
with open(output_file, "w") as f:
    for script in scripts:
        f.write(str(script))


# Extract the head-block
# ----------------------

# open index.html and read its contents
with open('index.html', 'r') as f:
    content = f.read()

# find the contents between <head> and </head>
start = content.find('<head>')
end = content.find('</head>') + len('</head>')
head_contents = content[start:end]

# write the contents to head-block.html in _includes directory without <head> and </head> tags
head_contents = head_contents.replace('<head>', '').replace('</head>', '')
with open('_includes/head-block.html', 'w') as f:
    f.write(head_contents)

# Extract the User-Blocks
# -----------------------

# Create the _includes directory if it doesn't exist
if not os.path.exists('_includes'):
    os.mkdir('_includes')

# Read the contents of the file
with open('index.html', 'r') as file:
    contents = file.readlines()

# Split the contents by the start and end markers
blocks = {}
for i in range(len(contents)):
    line = contents[i].strip()
    if line.startswith('<!-- ') and line.endswith(' START -->'):
        block_name = line[5:-10]
        blocks[block_name] = [contents[i-1], '']
    elif line.startswith('<!-- ') and line.endswith(' END -->'):
        block_name = line[5:-8]
        block_contents = blocks[block_name][1]
        file_name = block_name + '.html'
        file_path = os.path.join('_includes', file_name)
        with open(file_path, 'w') as block_file:
            block_file.write(blocks[block_name][0] + block_contents + line + '\n' + contents[i+1])
        blocks[block_name] = None
    else:
        for block_name in blocks.keys():
            if blocks[block_name] is not None:
                blocks[block_name][1] += line + '\n'


# Extract cookie-alert block
# --------------------------

# read in the HTML file
with open("index.html", "r") as f:
    html = f.read()

# create a BeautifulSoup object from the HTML
soup = BeautifulSoup(html, "html.parser")

# find the input tag with name attribute "cookieData"
input_tag = soup.find("input", {"name": "cookieData"})

# create the _includes folder if it doesn't exist
if not os.path.exists("_includes"):
    os.makedirs("_includes")

# write the input tag to the cookie-alert-block.html file in _includes
with open("_includes/cookie-alert-block.html", "w") as f:
    f.write(str(input_tag))

# Extract the mobirise-credit-block
# ---------------------------------

input_file = "index.html"
output_dir = "_includes"
output_file = "mobirise-credit-block.html"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(input_file, "r") as f:
    html = f.read()
    start_tag = "<section"
    end_tag = "</section>"
    start_index = html.find(start_tag)
    while start_index != -1:
        end_index = html.find(end_tag, start_index) + len(end_tag)
        section_block = html[start_index:end_index]
        if "HTML Website Generator" in section_block:
            with open(os.path.join(output_dir, output_file), "w") as out_f:
                out_f.write(section_block)
        start_index = html.find(start_tag, end_index)

# Copy templates
# --------------
# Set the paths for the folders
includes_folder = "_includes"
templates_folder = "_templates/contentblocks"

# Iterate through the files in the includes folder
for file_name in os.listdir(includes_folder):
    if file_name.endswith("template.html"):
        # If the file ends with "template.html", copy it to the templates folder
        file_path = os.path.join(includes_folder, file_name)
        shutil.copy(file_path, templates_folder)