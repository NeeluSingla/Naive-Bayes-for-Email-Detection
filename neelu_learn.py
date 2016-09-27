import os
import sys
import math

def learner(parentRootDirPath):
	spam = {}
	ham = {}
	total_spam = 0
	total_ham = 0
	parentRootDirPath = '/Users/Neelusingla/Desktop/train'
	for dirName, subdirList, fileList in os.walk(parentRootDirPath):
		for fname in fileList:
			if not fname.startswith('.'):
				if dirName.endswith('spam'):
					total_spam += 1
					with open(os.path.join(dirName,fname), "r", encoding='latin1') as file:
						for line in file:
							words = line.split()
							for word in words:
								if word not in spam:
									spam[word] = 1
								else:
									spam[word] += 1

				elif dirName.endswith('ham'):
					total_ham +=1
					with open(os.path.join(dirName,fname),"r",encoding='latin1') as file:
						for line in file:
							words=line.split()
							for word in words:
								if word not in ham:
									ham[word]= 1
								else:
									ham[word] +=1

	# Total number of distinct words in both the folders
	count=0
	Distinct_words=0
	for key in spam:
		if key not in ham:
			count= count+1
	
	Distinct_words=(len(ham)+count)

	#Probabilities calculation

	sys.stdout=open("nbmodel.txt","w")
	total_one=sum(spam.values())
	total_two=sum(ham.values())

	for key in spam:
		if key in ham:
			 print(key,((spam.get(key)+1)/(total_one+Distinct_words)),((ham.get(key)+1)/(total_two+Distinct_words)))
		else:
			 print(key,((spam.get(key)+1)/(total_one+Distinct_words)),(1/(total_two+Distinct_words)))
	for key in ham:
		if key not in spam:
			print(key,(1/(total_one+Distinct_words)),((ham.get(key)+1)/(total_two+Distinct_words)))
	sys.stdout.close()


if __name__=="__main__":
	learner(sys.argv[1]);