sudo docker run -it  --name="printsat-db" \
	-p 127.0.0.1:55432:5432 \
	--volumes-from printsat-data \
	cyface/printsat-db
