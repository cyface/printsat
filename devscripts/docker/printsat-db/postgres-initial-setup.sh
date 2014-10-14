#!/bin/bash
/usr/pgsql-9.3/bin/initdb -D /home/printsat/data/db
/usr/pgsql-9.3/bin/pg_ctl start -D /home/printsat/data/db/
sleep 5
psql --command "CREATE USER printsat WITH SUPERUSER PASSWORD 'printsat';"
createdb -O printsat printsat

echo "host all  all    0.0.0.0/0  md5" >> /home/printsat/data/db/pg_hba.conf
echo "listen_addresses='*'" >> /home/printsat/data/db/postgresql.conf

/usr/pgsql-9.3/bin/pg_ctl stop -D /home/printsat/data/db/
