sudo docker run \
	--rm \
	--volumes-from printsat-data \
	cyface/printsat-web \
	printsat-initial-setup.sh
