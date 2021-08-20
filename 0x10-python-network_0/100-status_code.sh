#!/bin/bash
# script comment
curl -so /dev/null --write-out "%{http_code}" "$1"
