FROM cyface/printsat-centos-base

MAINTAINER Tim L. White "tim@cyface.com"

USER root

# Add nginx official repository
ADD nginx.repo /etc/yum.repos.d/nginx.repo

# Install openssl
RUN yum install -y openssl-devel openssl

# Install nginx
RUN yum install -y --disablerepo=* --enablerepo=nginx nginx

# Turn off Daemon of nginx so that it can be managed by Docker
RUN echo -e "\ndaemon off;" >> /etc/nginx/nginx.conf

# Add Supervisor Config File for Printsat
ADD supervisord.conf /etc/nginx/supervisord.conf

# Delete default nginx configs
RUN rm /etc/nginx/conf.d/* 

# Add printsat nginx config
ADD printsat-nginx.conf /etc/nginx/conf.d/printsat-nginx.conf

# Add nginx to printsat group
RUN usermod -G printsat nginx

# Install uwsgi
RUN pip install uwsgi

# Switch to printsat user
USER printsat

# Add Printsat Uwsgi File
ADD printsat-uwsgi.xml /home/printsat/printsat-uwsgi.xml

# Switch to root to run supervisord
USER root

# Expose Web Port
EXPOSE 80

CMD ["supervisord", "-n", "-c", "/etc/nginx/supervisord.conf"]
