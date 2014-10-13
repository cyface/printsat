FROM cyface/printsat-centos-base

MAINTAINER Tim L. White "tim@cyface.com"

# Switch to printsat user
USER printsat

# Add Initial Clone Script
ADD printsat-initial-setup.sh /home/printsat/printsat-initial-setup.sh

CMD /home/printsat/printsat-initial-setup.sh 
