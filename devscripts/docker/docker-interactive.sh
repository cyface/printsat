#!/bin/bash
sudo docker run --rm --volumes-from printsat-data -it cyface/printsat-centos-base /bin/bash
