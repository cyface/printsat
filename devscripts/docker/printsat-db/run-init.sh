sudo docker run --rm \
	--volumes-from printsat-data \
	-it cyface/printsat-db \
	/home/printsat/postgres-initial-setup.sh
