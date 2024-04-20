#!/usr/bin/env bash

apt-get install nginx -y
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Everything is set up perfectly" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/current /data/web_static/releases/test/
chown ubuntu:ubuntu -R /data

hbnb_static_alias="location \/hbnb_static\/ \{\nalias \/data\/web_static\/current\/\;autoindex off\;\n\}"
sed -i "/root/a $hbnb_static_alias" /etc/nginx/sites-available/getalien.tech
nginx -s reload
