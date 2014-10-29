#!/bin/bash
cd /home/printsat/data/printsat
su printsat -c "git pull"
su printsat -c "touch printsat/local_settings.py"
