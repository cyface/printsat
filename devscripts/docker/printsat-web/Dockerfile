FROM podiobooks/centos-nginx-uwsgi

MAINTAINER Tim L. White "tim@cyface.com"

# Install Virtualenv and Supervisor
RUN pip install virtualenv supervisor

# Add Supervisor Config File for Printsat
ADD supervisord.conf /etc/nginx/supervisord.conf

# Delete default nginx configs
RUN rm /etc/nginx/conf.d/* 

# Add printsat nginx config
ADD printsat-nginx.conf /etc/nginx/conf.d/printsat-nginx.conf

# Create printsat user
RUN useradd printsat

# Add nginx to printsat group
RUN usermod -G printsat nginx

# Open group permissions to printsat home dir
RUN chmod g+rx /home/printsat

# Switch to printsat user
USER printsat

# Add Printsat Uwsgi File
ADD printsat-uwsgi.xml /home/printsat/printsat-uwsgi.xml

# Change to printsat dir
WORKDIR /home/printsat

# git checkout printsat
RUN git clone https://github.com/cyface/printsat.git

# Move to Code Dir
WORKDIR /home/printsat/printsat

# Switch Back to Root
USER root

# Install Dependencies
RUN pip install -r /home/printsat/printsat/requirements.txt

# Switch Back to Printsat
USER printsat

# Initialize DB
RUN python manage.py syncdb --noinput
RUN python manage.py collectstatic --noinput

# And back to root again
USER root

# Add logs dir
RUN mkdir logs

# Expose Log Dir
VOLUME /home/printsat/logs

# Start uWSGI
CMD ["supervisord", "-n", "-c", "/etc/nginx/supervisord.conf"]
