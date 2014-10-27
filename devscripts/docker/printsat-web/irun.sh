sudo docker run --rm -it \
	--volumes-from printsat-data \
	--link printsat-db:db \
	cyface/printsat-web /bin/bash
