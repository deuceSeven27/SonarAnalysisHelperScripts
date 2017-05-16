#!/bin/bash

if [ $# -lt 2 ]; then
echo Usage: ./extractToFolder inputPath outputPath
exit 1
fi

mkdir $2/extractedFiles

mkdir $2/temp

for file in $(ls $1 | grep tgz); do
	
	echo processing $file...
	fileName="$(echo $file | cut -d'.' -f 1)" #${file:0:8}
	echo $fileName

	#extract file to temp folder
	tar -xvzf $1/$file -C $2/temp

	mkdir $2/extractedFiles/$fileName
	mv $2/temp/* $2/extractedFiles/$fileName

done

rm -r $2/temp
