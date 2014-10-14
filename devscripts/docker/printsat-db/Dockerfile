FROM cyface/printsat-centos-base

MAINTAINER Tim L. White "tim@cyface.com"

# Install Prereqs
RUN yum install -y libxslt uuid

# Install PostgreSQL
RUN yum install -y postgresql-server postgresql-libs postgresql-contrib postgresql-devel --disablerepo=* --enablerepo=postgresql

# Add Postgres User to Printsat Group
RUN usermod -G printsat postgres

# Switch to postgres user
USER postgres

# Add postgres init file
ADD postgres-initial-setup.sh /home/printsat/postgres-initial-setup.sh

# Expose Ports
EXPOSE 5432

# Start uWSGI
CMD ["/usr/pgsql-9.3/bin/pg_ctl", "start", "-D", "/home/printsat/data/db/", "-l", "/home/printsat/data/postgres.log", "-s", "-w", "-t", "300"]
