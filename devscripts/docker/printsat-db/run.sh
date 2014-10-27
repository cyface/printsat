sudo docker run -d --name="printsat-db" \
	--volumes-from printsat-data \
	cyface/printsat-db
