from bs4 import BeautifulSoup
import os
import re

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
                       {% unless page.menutitle == null or page.hide or name_page contains page.title %}
                       <li class="nav-item"><a class="nav-link link text-black display-4" href="{{ page.url }}">{{ page.title }}</a></li>
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