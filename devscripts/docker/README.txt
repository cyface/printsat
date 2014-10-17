Here's how to get this all up and going with Docker.

0) Build all your images by going into each subfolder and running the 'build.sh' script in there.

1) Get your data container going by running the 'run.sh' in the printsat-data folder.  That will create a container, but it immediately quits.  That's OK, it doesn't need to stay running to hold it's volumes open.

2) Set up the DB container by running 'run-init.sh' in the printsat-db folder. That will start up the PostgreSQL server just long enough to set up the configs, and then quit.

3) Fire up the DB by running 'run.sh' in the printsat-db folder, this will start up the database to run as a docker daemon.

4) Set up the web by doing the 'run-init.sh' script in the printsat-web folder - this will check out the code, etc.

5) Use the 'irun.sh' to go into a temp copy of the printsat-web container and then:
   A) su - printsat
   B) cd /home/printsat/data/printsat
   C) vi local_settings.py and replace <CHANGEME> with a new password of your choosing.
   D) psql -h db -U printsat (pw is printsat) to get into postgres, and then use ALTER USER printsat PASSWORD <newpw>; to set your new password. 
   E) Use \q to exit psql.
   F) . .env/bin/activate
   G) python manage.py syncdb   to init the database in postgres.
   H) Exit out of the temp container with 'exit'.

6) Fire up the web tier with 'run.sh' int he printsat-web folder.

7) You can use the docker-interactive-shell.sh or the irun.sh scripts to get into a container that will let you take a look at the /home/printsat/data dir which has all logs - you can also use it to pull code updates, export backups, etc.

Enjoy !


