if [ $# -ne 1 ]; then
	echo Usage: ./passAllToSnq.sh pathToSonarScannerBinFolder
exit 1
fi

origin=$PWD

find ../srcCode/ -type d -name extractedFiles | while read line; do
	echo '#################### Running Sonar-Scanner for $line ####################'
	cd $line;
	$1/sonar-scanner;
	cd $origin;
done

echo 'complete!'