sudo docker run \
	--rm \
	--volumes-from printsat-data \
	cyface/printsat-web \
	/home/printsat/printsat-initial-setup.sh
