#!/bin/bash
if [ -d /home/printsat/data/printsat ]; then 
	rm -rf /home/printsat/data/printsat
fi
git clone https://github.com/cyface/printsat.git /home/printsat/data/printsat
cd /home/printsat/data/printsat
./devscripts/virtualenv/setup_prod_env.sh
. .env/bin/activate
python manage.py collectstatic --noinput
chown -R printsat.printsat /home/printsat/data