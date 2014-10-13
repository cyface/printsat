FROM centos:latest 

MAINTAINER Tim L. White "tim@cyface.com"

# Setup PostgreSQL Repo
RUN rpm -Uvh http://yum.postgresql.org/9.3/redhat/rhel-7-x86_64/pgdg-centos93-9.3-1.noarch.rpm

# Install Prereqs
RUN yum install -y libxslt uuid

# Install PostgreSQL
RUN yum install -y libxslt postgresql93 postgresql93-server postgresql93-libs postgresql93-contrib postgresql93-devel --disablerepo=* --enablerepo=pgdg93
#RUN /usr/pgsql-9.3/bin/postgresql93-setup initdb
#RUN chmod 700 /var/lib/pgsql/9.3/data

# Install Supervisor
RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install supervisor 

# Add Supervisor Config File for Printsat
ADD supervisord.conf /etc/supervisord.conf

# Expose Volumes
#VOLUME ["/data", "/var/log/postgresql", "/etc/postgresql", "/var/lib/pgsql/9.3/data/"]

# Expose Ports
EXPOSE 5432

# Start uWSGI
CMD ["supervisord", "-n", "-c", "/etc/supervisord.conf"]
