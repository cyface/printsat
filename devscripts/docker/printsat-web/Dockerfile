FROM podiobooks/centos-nginx-uwsgi

MAINTAINER Tim L. White "tim@cyface.com"

# Install Virtualenv and Supervisor
RUN pip install virtualenv supervisor

# Add Supervisor Config File for Printsat
ADD supervisord.conf /etc/supervisor/conf.d/

# Create printsat user
RUN useradd printsat

# Switch to printsat user
USER printsat

# Change to printsat dir
WORKDIR /home/printsat

# Add printsat uWSGI config file
ADD printsat-uwsgi.xml /home/printsat/printsat-uwsgi.xml

# git checkout printsat
RUN git clone https://github.com/cyface/printsat.git

# Move to Code Dir
WORKDIR /home/printsat/printsat

# Install Code Dependencies
RUN devscripts/virtualenv/setup_prod_env.sh

# Activate Virtualenv
RUN . .env/bin/activate

# Initialize DB
RUN python manage.py syncdb --noinput

# Add logs dir
RUN mkdir logs

# Expose Log Dir
VOLUME /home/printsat/logs

# Start uWSGI
CMD ["supervisord", "-n"]
