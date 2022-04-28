#!/usr/bin/env bash
# Install NGINX
sudo apt-get update
sudo apt-get install nginx -y
sudo ufw allow 'Nginx HTTP'
sudo ufw enable
echo Hello World | sudo tee /var/www/html/index.nginx-debian.html
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir /data/web_static/shared/
echo HelloWorld | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/server_name _;/a\location \/hbnb_static\/ {\n alias \/data\/web_static\/current\/;\n}' /etc/nginx/sites-available/default
sudo service nginx restart
