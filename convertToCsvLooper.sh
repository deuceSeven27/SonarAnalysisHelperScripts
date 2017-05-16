ls ../snqHtmls/*.html | while read line; do echo $line; python convertSnqToCsv.py $line; done
