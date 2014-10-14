FROM cyface/printsat-centos-base

MAINTAINER Tim L. White "tim@cyface.com"

# Install Prereqs
RUN yum install -y libxslt uuid

# Install PostgreSQL
RUN yum install -y postgresql-server postgresql-libs postgresql-contrib postgresql-devel --disablerepo=* --enablerepo=postgresql

# Add Postgres User to Printsat Group
RUN usermod -G printsat postgres

# Add Supervisor Config File for Printsat
ADD supervisord.conf /etc/supervisord.conf

# Add postgres init file
ADD postgres-initial-setup.sh /home/printsat/postgres-initial-setup.sh
RUN chown printsat.printsat /home/printsat/postgres-initial-setup.sh

# Expose Ports
EXPOSE 5432

# Start uWSGI
CMD ["supervisord", "-n", "-c", "/etc/supervisord.conf"]
