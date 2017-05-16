import os

keywords = ["Socks", "NumberExchange", "PrimeCount", "NumberofFiboCalls", "TwiceString", "DucksAlignment", "MarbleNecklace", "EmoticonsDiv2", "Egalitarianism"]

kwCounter = 0

for exam in xrange(1,4):
	for question in xrange(1,4):

		assignmentFolderName = "pracexam" + str(exam) + "p" + str(question)
		print("Doing " + assignmentFolderName + ", keyword is " + keywords[kwCounter])
		#called from the helperScripts folder
		os.system("./removeUntestedFiles.sh ../srcCode/" + assignmentFolderName + "/extractedFiles/ " + keywords[kwCounter])
		kwCounter = kwCounter + 1

#add a dummy file if we deleted the entire submission dir for student
#(for students who attempt question but fail)
print "adding dummy files to empty submission folders..."
os.system("find ../srcCode/ -type d -empty -iname 'a[0-9]*_[0-9]*' | while read line; do touch $line/DummyFile.cpp && echo //this is a dummy file >> $line/DummyFile.cpp; done")

print "added dummy files to empty submission folder..."

#find and delete all empty directories
os.system("find ../srcCode/ -type d -empty -delete") 

print "Completed!"