sudo docker run --rm -it --volume="$PWD:/root/html" -p 4100:4000 ramirezfx/docker-jekyll:latest /bin/sh -c "cd /root/html && bundle exec jekyll serve --host 0.0.0.0"
