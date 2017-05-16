#this converts a sonarqube analysis page to a csv file. 
import sys
from bs4 import BeautifulSoup

#line like a1668979_100/Socks.hpp3
def getTitleMarkMetric(input):

	trEntry = ''.join(input.split())
	
	splitIndex = len(trEntry) - 1

	#splitting the title and metric
	for index in range(len(trEntry) - 1, -1, -1):
		if trEntry[index].isdigit():
			splitIndex = splitIndex - 1
		else:
			break

	#get the mark
	mark = trEntry.split("_")[1].split("/")[0]

	return (trEntry[0:splitIndex + 1],  trEntry[splitIndex + 1 : len(trEntry)], mark)




if len(sys.argv) < 1:
	print "Usage: python convertSnqToCsv.py [input SonarQube html page]"
	sys.exit()


print "processing " + sys.argv[1] + "..."

htmlString = ""

with open(sys.argv[1], 'r') as file:
	htmlString = file.read().replace("\n", "")

htmlParsed = BeautifulSoup(htmlString, 'html.parser')

#print( htmlParsed.prettify())

fileAndMetric = []

#line like a1668979_100/Socks.hpp3
for line in htmlParsed.find_all('tr'):

	fileAndMetric.append(getTitleMarkMetric(line.get_text()))

#../snqHtmls/pracexam1p1.html
# parts = sys.argv[1].split("/")
# filename = parts[-1].split(".")[0]
# print filename

output = open(sys.argv[1] + ".csv", "wb")

for item in fileAndMetric:
	output.write(item[0] + ", " + item[1] +", " + item[2] +"\n" ) 

print "Program complete..."