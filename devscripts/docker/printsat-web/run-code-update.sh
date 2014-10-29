sudo docker run \
	--rm \
	--volumes-from printsat-data \
	cyface/printsat-web \
	/home/printsat/printsat-code-update.sh
