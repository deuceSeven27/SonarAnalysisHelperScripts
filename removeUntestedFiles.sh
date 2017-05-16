#!/bin/bash
#this finds and removes all files that do not contain a keyword
if [ $# -ne 2 ]; then
    echo Usage: ./removeUntestedFiles [root directory] [keyword]
    exit 1
fi

#find all .hpp files, then remove all files that dont 
#match the provided keywords
find $1 -type f | grep -iv $2.hpp$ | while read line; do
	echo removing $line
	rm $line
done
