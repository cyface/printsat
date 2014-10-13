FROM cyface/printsat-centos-base

MAINTAINER Tim L. White "tim@cyface.com"

USER printsat

ADD fix-data-volume-permissions.sh /home/printsat/fix-data-volume-permissions.sh

# Make a directory to use
RUN mkdir /home/printsat/data

# Expose Volume for Cther Containers to Grab Onto
VOLUME ["/home/printsat/data"]

CMD ["/home/printsat/fix-data-volume-permissions.sh"]

