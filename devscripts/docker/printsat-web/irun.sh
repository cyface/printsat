sudo docker run -it \
	--volumes-from printsat-data \
	--link printsat-db:db \
	cyface/printsat-web /bin/bash
