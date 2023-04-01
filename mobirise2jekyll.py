from bs4 import BeautifulSoup
import os
import shutil
import re
# Create the base folder layout for jeckyll
# -----------------------------------------

# folders = ["_includes", "_data", "_layouts", "_posts", "_templates", "_templates/contentblocks", "pages"]

# for folder in folders:
#     if not os.path.exists(folder):
#         os.makedirs(folder)

# Copy from source to working-dir:
# --------------------------------

source_dir = '_html-source'
for item in os.listdir(source_dir):
    if item != 'readme.md':
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(os.getcwd(), item)
        shutil.move(source_path, dest_path)

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

with open('index.html', 'r') as f:
    index_html = f.read()

head_start = '<head>'
head_end = '</head>'
head_start_index = index_html.find(head_start)
head_end_index = index_html.find(head_end)

head_content = index_html[head_start_index+len(head_start):head_end_index]

with open('_includes/head-block.html', 'r+') as f:
    head_block_html = f.read()
    insert_index = head_block_html.find('<!-- Paste Your HEAD-HTML-Code Here -->') + len('<!-- Paste Your HEAD-HTML-Code Here -->')
    f.seek(insert_index)
    existing_content = f.read()
    f.seek(insert_index)
    f.write('\n' + head_content + '\n' + existing_content)
    
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

# MODIFY USER-BLOCKS:
# -------------------

# head-block.html
# ---------------
# Open the head-block.html file for reading
with open('_includes/head-block.html', 'r') as file:
    # Read the contents of the file into a string variable
    contents = file.read()

# Replace the existing shortcut icon line with the new code-snippet
new_contents = contents.replace('<link rel="shortcut icon" data-href="/assets/images/logo.png" type="image/x-icon">', '{% if site.faviconpath %}\n<link rel="shortcut icon" data-href="{{ site.faviconpath }}" type="image/x-icon" />\n{% endif %}')

# Open the head-block.html file for writing
with open('_includes/head-block.html', 'w') as file:
    # Write the updated contents back to the file
    file.write(new_contents)

# header-block.html
# -----------------

# Replace Path To Logo-Image
file_path = '_includes/header-block.html'
img_path_to_replace = '/assets/images/logo.png'
new_img_path = '{{ site.imglogopath }}'

with open(file_path, 'r') as file:
    contents = file.read()

new_contents = contents.replace(img_path_to_replace, new_img_path)

with open(file_path, 'w') as file:
    file.write(new_contents)

# Replace Link Of Logo-Image

# Read the HTML file
with open("_includes/header-block.html", "r") as f:
    html = f.read()

# Parse the HTML with Beautiful Soup
soup = BeautifulSoup(html, "html.parser")

# Find the img element
img = soup.find("img")

# Find the corresponding a element and replace its href attribute with "/"
a = img.find_parent("a")
a["href"] = "/"

# Save the modified HTML back to the file
with open("_includes/header-block.html", "w") as f:
    f.write(str(soup))

# Read the contents of the header-block.html file
with open('_includes/header-block.html', 'r') as f:
    html = f.read()

# Parse the HTML string
soup = BeautifulSoup(html, 'html.parser')

# Get the list of all list-items
list_items = soup.select('.navbar-nav li')

# Loop through all list-items, starting from the second one
for item in list_items[1:]:
    # Remove the current list-item from the DOM
    item.extract()

# Write the modified HTML back to the header-block.html file
with open('_includes/header-block.html', 'w') as f:
    f.write(str(soup))

# NEXT
import os

# Define the path to the HTML file
html_file_path = '_includes/header-block.html'

# Define the code to insert
code_to_insert = '''{% assign name_page = "" %}
                   {% for page in site.pages %}
                       {% unless page.menutitle == null or page.hide or name_page contains page.menutitle %}
                       <li class="nav-item"><a class="nav-link link text-black display-4" href="{{ page.url }}">{{ page.menutitle }}</a></li>
                       {% endunless %}
                       {% assign name_page = page.menutitle | append: name_page %}
                   {% endfor %}'''

# Read the contents of the HTML file
with open(html_file_path, 'r') as f:
    file_contents = f.read()

# Find the index of the </ul> tag
ul_tag_index = file_contents.find('</ul>')

# Insert the code before the </ul> tag
new_file_contents = file_contents[:ul_tag_index] + code_to_insert + file_contents[ul_tag_index:]

# Replace [LISTELEMENT] with the code to insert
new_file_contents = new_file_contents.replace('[LISTELEMENT]', code_to_insert)

# Overwrite the original HTML file with the modified contents
with open(html_file_path, 'w') as f:
    f.write(new_file_contents)
# NEXT

# Define the path to the HTML file
html_file_path = '_includes/header-block.html'

# Read the contents of the HTML file
with open(html_file_path, 'r') as f:
    file_contents = f.read()

# Find the first <li> element
li_start_index = file_contents.find('<li')

# Find the corresponding </li> element
li_end_index = file_contents.find('</li>', li_start_index) + len('</li>')

# Remove the first <li></li> element
new_file_contents = file_contents[:li_start_index] + file_contents[li_end_index:]

# Overwrite the original HTML file with the modified contents
with open(html_file_path, 'w') as f:
    f.write(new_file_contents)

# NEXT

# Define the path to the HTML file
file_path = '_includes/header-block.html'

# Read the contents of the file into a string
with open(file_path, 'r') as f:
    file_contents = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(file_contents, 'html.parser')

# Find all a elements containing {{ site.sitename }}
for a_tag in soup.find_all('a', string='{{ site.sitename }}'):
    # Replace the href attribute value with a forward slash
    a_tag['href'] = '/'

# Write the modified file contents back to the file
with open(file_path, 'w') as f:
    f.write(str(soup))

# Load the HTML file
with open('_includes/cycling-block.html', 'r') as f:
    html = f.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find the first cycling block
cycling_blocks = soup.select('.item.features-image')
if len(cycling_blocks) > 0:
    first_cycling_block = cycling_blocks[0]
    # Remove all other cycling blocks
    for cycling_block in cycling_blocks[1:]:
        cycling_block.decompose()
        
# Save the modified HTML
with open('_includes/cycling-block.html', 'w') as f:
    f.write(str(soup))

html_file_path = '_includes/cycling-block.html'

# Load the HTML file into BeautifulSoup
with open(html_file_path, 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find the div with the class "item features-image"
div = soup.find('div', {'class': re.compile(r'\bitem features-image\b.*')})
if not div:
    raise ValueError('Could not find div with class "item features-image"')

# Insert the code before and after the div
div.insert_before('{% for post in paginator.posts %}')
div.insert_after('{% endfor %}')

# Overwrite the original HTML file with the modified HTML
with open(html_file_path, 'w') as f:
    f.write(str(soup))

# Path to the HTML file to be modified
file_path = '_includes/cycling-block.html'

# Read the content of the file into a string
with open(file_path, 'r') as f:
    content = f.read()

# Use regular expressions to find and replace the value of data-src
new_content = re.sub(r'data-src="[^"]+"', r'data-src="{{ post.thumbnail }}"', content)

# Write the modified content back to the file
with open(file_path, 'w') as f:
    f.write(new_content)

# Delete index.html and replace it with index-new.html
# ----------------------------------------------------
# define the file names
old_file = "index.html"
new_file = "index-new.html"

# delete the old file
if os.path.exists(old_file):
    os.remove(old_file)
    print(f"{old_file} deleted.")
else:
    print(f"{old_file} does not exist.")

# rename the new file to the old file name
if os.path.exists(new_file):
    os.rename(new_file, old_file)
    print(f"{new_file} renamed to {old_file}.")
else:
    print(f"{new_file} does not exist.")
