import os

for exam in xrange(1,4):
	for question in xrange(1,4):
		assignmentFolderName = "pracexam" + str(exam) + "p" + str(question)
		os.system("touch ../srcCode/" + assignmentFolderName + "/extractedFiles/sonar-project.properties && echo 'sonar.projectKey=" + assignmentFolderName + "\nsonar.projectName=" + assignmentFolderName + "\nsonar.projectVersion=1.0\nsonar.sources=.' >> ../srcCode/" + assignmentFolderName + "/extractedFiles/sonar-project.properties")