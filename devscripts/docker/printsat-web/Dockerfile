FROM podiobooks/centos-nginx-uwsgi

MAINTAINER Tim L. White "tim@cyface.com"

# Run Nginx
CMD "nginx"

# Create printsat user
RUN useradd printsat

# Switch to printsat user
USER printsat

# Change to printsat dir
WORKDIR /home/printsat

# git checkout printsat
RUN git clone https://github.com/cyface/printsat.git

# Add printsat uWSGI config file
ADD printsat-uwsgi.xml /home/printsat/printsat-uwsgi.xml

# Add logs dir
RUN mkdir logs

# Expose Log Dir
VOLUME /home/printsat/logs

# Start uWSGI
CMD uwsgi --xml printsat-uwsgi.xml
