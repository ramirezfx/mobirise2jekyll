import urllib.request
import os

url = "https://github.com/ramirezfx/jekyll-template/raw/master/Gemfile"
filename = "Gemfile"
urllib.request.urlretrieve(url, filename)

url = "https://github.com/ramirezfx/jekyll-template/raw/master/_config.yml"
filename = "_config.yml"
urllib.request.urlretrieve(url, filename)

url = "https://github.com/ramirezfx/jekyll-template/raw/master/1startproject-docker.sh"
filename = "1startproject-docker.sh"
urllib.request.urlretrieve(url, filename)
current_permissions = os.stat(filename).st_mode
new_permissions = current_permissions | 0o100
os.chmod(filename, new_permissions)


url = "https://github.com/ramirezfx/jekyll-template/raw/master/1startproject.sh"
filename = "1startproject.sh"
urllib.request.urlretrieve(url, filename)
current_permissions = os.stat(filename).st_mode
new_permissions = current_permissions | 0o100
os.chmod(filename, new_permissions)

url = "https://github.com/ramirezfx/jekyll-template/raw/master/index.html"
filename = "index.html"
urllib.request.urlretrieve(url, filename)

url = 'https://github.com/ramirezfx/jekyll-template/raw/master/_layouts/frontpage.html'
folder = '_layouts'
filename = 'frontpage.html'
urllib.request.urlretrieve(url, os.path.join(folder, filename))

url = 'https://github.com/ramirezfx/jekyll-template/raw/master/_layouts/page.html'
folder = '_layouts'
filename = 'page.html'
urllib.request.urlretrieve(url, os.path.join(folder, filename))

url = 'https://github.com/ramirezfx/jekyll-template/raw/master/_layouts/search.html'
folder = '_layouts'
filename = 'search.html'
urllib.request.urlretrieve(url, os.path.join(folder, filename))

url = 'https://github.com/ramirezfx/jekyll-template/raw/master/_layouts/tags.html'
folder = '_layouts'
filename = 'tags.html'
urllib.request.urlretrieve(url, os.path.join(folder, filename))

url = 'https://github.com/ramirezfx/jekyll-template/raw/master/pages/search.html'
folder = 'pages'
filename = 'search.html'
urllib.request.urlretrieve(url, os.path.join(folder, filename))

url = 'https://github.com/ramirezfx/jekyll-template/raw/master/pages/tags.html'
folder = 'pages'
filename = 'tags.html'
urllib.request.urlretrieve(url, os.path.join(folder, filename))

url = 'https://github.com/ramirezfx/jekyll-template/raw/master/_includes/page-content.html'
folder = '_includes'
filename = 'page-content.html'
urllib.request.urlretrieve(url, os.path.join(folder, filename))

url = 'https://github.com/ramirezfx/jekyll-template/raw/master/_includes/frontpage-content.html'
folder = '_includes'
filename = 'frontpage-content.html'
urllib.request.urlretrieve(url, os.path.join(folder, filename))

url = 'https://github.com/ramirezfx/jekyll-template/raw/master/_includes/pagination-navigation.html'
folder = '_includes'
filename = 'pagination-navigation.html'
urllib.request.urlretrieve(url, os.path.join(folder, filename))

url = 'https://github.com/ramirezfx/jekyll-template/raw/master/_includes/tag-list.html'
folder = '_includes'
filename = 'tag-list.html'
urllib.request.urlretrieve(url, os.path.join(folder, filename))

url = 'https://github.com/ramirezfx/jekyll-template/raw/master/_includes/post-info.html'
folder = '_includes'
filename = 'post-info.html'
urllib.request.urlretrieve(url, os.path.join(folder, filename))