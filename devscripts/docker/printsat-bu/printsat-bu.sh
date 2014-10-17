#!/bin/bash
mkdir /home/printsat/.ssh/
echo -e "Host github.com\n\tStrictHostKeyChecking no\n" >> /home/printsat/.ssh/config
ssh-agent bash -c 'ssh-add /home/printsat/data/.ssh/id_rsa; git clone git@github.com:cyface/printsat_bu.git /home/printsat/data/printsat_bu'
cd /home/printsat/data/printsat
. .env/bin/activate
python manage.py dumpdata printsat_app > /home/printsat/data/printsat_bu/alldata.json
gzip --quiet --force /home/printsat/data/printsat_bu/alldata.json
cd /home/printsat/data/printsat_bu
git add *
git config user.email "tim@cyface.com"
git config user.name "Printsat BU"
git config push.default simple
git commit -am "Backup"
ssh-agent bash -c 'ssh-add /home/printsat/data/.ssh/id_rsa; git push'
