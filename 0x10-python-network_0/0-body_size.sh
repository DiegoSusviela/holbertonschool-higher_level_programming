#!/bin/bash
# script yeah man
curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2
