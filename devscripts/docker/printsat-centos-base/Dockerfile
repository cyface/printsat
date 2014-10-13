FROM centos:latest

MAINTAINER Tim L. White "tim@cyface.com"

# Add repos for other items
ADD epel.repo /etc/yum.repos.d/epel.repo
ADD postgresql.repo /etc/yum.repos.d/postgresql.repo
ADD CentOS-fasttrack.repo /etc/yum.repos.d/CentOS-fasttrack.repo

# Update centos
RUN yum upgrade -y

# Install compiler
RUN yum install -y gcc 

# Reqs needed for uwsgi (and others)
RUN yum install -y python-devel libxml2-devel pcre-devel jansson-devel libcap-devel uuid-devel sqlite-devel openldap-devel libyaml-devel

# Install & Upgrade pip
RUN yum install -y --nogpgcheck python-pip
RUN pip install --upgrade pip

# Install Postgres Client Libs & Psycopg2
RUN yum install -y --disablerepo=* --enablerepo=postgresql postgresql-devel
RUN ln -s /usr/pgsql-9.3/bin/pg_config /usr/local/bin/pg_config
RUN pip install psycopg2

# Install Pillow
RUN yum install -y libjpeg libjpeg-devel zlib zlib-devel libtiff libtiff-devel libfreetype libfreetype-devel littlecms littlecms-devel libwebp libwebp-devel openjpeg openjpeg-devel

# Install git
RUN yum install -y git

# Install virtualenv
RUN pip install virtualenv

# Install supervisor
RUN pip install supervisor

# Create printsat user
RUN useradd -u 451 printsat -d /home/printsat -c "Printsat User"
RUN chown -R printsat.printsat /home/printsat
RUN chmod -R g+rwx /home/printsat

# Default Command
CMD ["/bin/bash"]
