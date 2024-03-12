#!/usr/bin/env bash
# A Bash script that sets up web servers for the deployment of web_static

apt-get -y update > /dev/null
apt-get install -y nginx > /dev/null

# Creates all necessary directories and file
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "Hello World again!" > /data/web_static/releases/test/index.html

# Checks if directory current exist
if [ -d "/data/web_static/current" ]
then
        sudo rm -rf /data/web_static/current
fi

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -hR ubuntu:ubuntu /data

# Configure nginx to serve content pointed to by symbolic link to hbnb_static
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

service nginx restart
