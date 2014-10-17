FROM cyface/printsat-centos-base

MAINTAINER Tim L. White "tim@cyface.com"

USER root

# Install uwsgi
RUN yum install -y python-devel libxml2-devel pcre-devel jansson-devel libcap-devel uuid-devel sqlite-devel openldap-devel libyaml-devel
RUN pip install uwsgi

# Install Psycopg2
RUN pip install psycopg2

# Install Pillow
RUN yum install -y libjpeg libjpeg-devel zlib zlib-devel libtiff libtiff-devel libfreetype libfreetype-devel littlecms littlecms-devel libwebp libwebp-devel openjpeg openjpeg-devel

# Install virtualenv
RUN pip install virtualenv

# Add nginx official repository
ADD nginx.repo /etc/yum.repos.d/nginx.repo

# Install openssl
RUN yum install -y openssl-devel openssl

# Install nginx
RUN yum install -y --disablerepo=* --enablerepo=nginx nginx

# Turn off Daemon of nginx so that it can be managed by Docker
RUN echo -e "\ndaemon off;" >> /etc/nginx/nginx.conf

# Delete default nginx configs
RUN rm /etc/nginx/conf.d/* 

# Add Supervisor Config File for Printsat
ADD supervisord.conf /etc/nginx/supervisord.conf

# Add printsat nginx config
ADD printsat-nginx.conf /etc/nginx/conf.d/printsat-nginx.conf

# Add nginx to printsat group
RUN usermod -G printsat nginx

# Switch to printsat user
USER printsat

# Add Printsat Uwsgi File
ADD printsat-uwsgi.xml /home/printsat/printsat-uwsgi.xml

# Add setup script
ADD printsat-initial-setup.sh /home/printsat/printsat-initial-setup.sh

# Add local app settings file to temp location - init setup will install
ADD printsat_local_settings.py /home/printsat/local_settings.py

# Switch to root to run supervisord
USER root

# Expose Web Port
EXPOSE 80

CMD ["supervisord", "-n", "-c", "/etc/nginx/supervisord.conf"]
