sudo docker run -d --name="printsat-web" \
	-p 127.0.0.1:50000:80 \
	--link printsat-db:db \
	--volumes-from printsat-data \
	cyface/printsat-web
