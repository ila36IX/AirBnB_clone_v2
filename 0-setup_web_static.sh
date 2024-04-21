#!/usr/bin/env bash
# Sets up the web servers for the deployment of web_static
# Install nginx
sudo apt-get install nginx -y

# Create the essentails directories
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "Everything is set up perfectly" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give the ubuntu user the ownership of /data/
sudo chown -R ubuntu:ubuntu /data

# Update the Nginx configuration to serve the content of
# /data/web_static/current/ to hbnb_static.
if [ "$(grep -c "location /hbnb_static" /etc/nginx/sites-available/getalien.tech)" -ne 1 ]
then
	hbnb_static_alias="location \/hbnb_static \{\nalias \/data\/web_static\/current\/\;autoindex off\;\n\}"
	sudo sed -i "/root/a $hbnb_static_alias" /etc/nginx/sites-available/getalien.tech
fi
sudo nginx -s reload
