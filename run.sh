#!/bin/bash -l
cd $(dirname $0)
/usr/bin/docker build -t penguincoder/godaddy-dns .
/usr/bin/docker run --rm -e API_KEY=$API_KEY -e API_SECRET=$API_SECRET -it penguincoder/godaddy-dns
