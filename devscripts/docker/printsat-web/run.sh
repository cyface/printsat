mkdir /tmp/printsat-web
mkdir /tmp/printsat-web/logs
sudo docker run -d --name="printsat-web" \
	-p 127.0.0.1:50000:80 \
	-v /tmp/printsat-web/logs:/var/log/nginx \
	cyface/printsat-web
