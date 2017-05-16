#quick script to automate extraction for all files using my extractToFolder 
#bash script
import os
for examNum in range(1,4):
	for qNum in range(1,4):
		examQuestion = "pracexam" + str(examNum) + "p" + str(qNum)
		os.system("./extractToFolder.sh ../srcCode/" + examQuestion + "/tarGets/ ../srcCode/" + examQuestion + "/")