#!/usr/bin/env bash
# Sets up the web servers for the deployment of web_static
# Install nginx
apt-get install nginx -y

# Create the essentails directories
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Everything is set up perfectly" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/current /data/web_static/releases/test/
# Give the ubuntu user the ownership of /data/
chown ubuntu:ubuntu -R /data

# Update the Nginx configuration to serve the content of
# /data/web_static/current/ to hbnb_static.
hbnb_static_alias="location \/hbnb_static\/ \{\nalias \/data\/web_static\/current\/\;autoindex off\;\n\}"
sed -i "/root/a $hbnb_static_alias" /etc/nginx/sites-available/getalien.tech
nginx -s reload
