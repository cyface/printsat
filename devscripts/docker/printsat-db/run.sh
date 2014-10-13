mkdir /tmp/printsat-db
mkdir /tmp/printsat-db/logs
sudo docker run -d --name="printsat-db" \
	-p 127.0.0.1:55432:5432 \
	-v /tmp/printsat-db/logs:/var/log/postgresql \
	-it cyface/printsat-db
