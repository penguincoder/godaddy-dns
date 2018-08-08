#!/bin/bash
DOCKER=$(/usr/bin/env docker)
cd $0
$DOCKER built -t penguincoder/godaddy-dns .
$DOCKER run --rm -it penguincoder/godaddy-dns
