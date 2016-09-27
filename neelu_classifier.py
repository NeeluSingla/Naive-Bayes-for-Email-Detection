import os
import sys
import math

def classifier(parentRootDirPath):
	array=[]
	total_spam=0
	total_ham =0
	map={}
	true_positive=0
	False_positive=0
	True_Negative=0
	False_Negative=0
	recall=0.0
	precision=0.0
	F_Score=0.0

	for dirName, subdirList, fileList in os.walk(parentRootDirPath):
		#print('Found directory: %s' % dirName)
		for fname in fileList:
			if not fname.startswith('.'):
				if dirName.endswith('spam'):
					total_spam += 1
				elif dirName.endswith('ham'):
					total_ham += 1
	prior_spam=math.log(float(total_spam/(total_ham+total_spam)))
	prior_ham=math.log(float(total_ham/(total_ham+total_spam)))

	with open("neelu_model.txt", "r+") as f:
                fp=open('nboutput.txt', 'w')
		for line in f:
			array=line.split()
			map[array[0]]=array

	count_spam=0
	count_ham=0
	prob_spam=0.0
	prob_ham=0.0
	parentRootDirPath = '/Users/Neelusingla/Desktop/dev'
	for dirName, subdirList, fileList in os.walk(parentRootDirPath):
		for fname in fileList:
			if not fname.startswith('.'):

				with open(os.path.join(dirName, fname), "r", encoding='latin1') as file:
					total_spam_prob=0.0
					total_ham_prob=0.0
					for line in file:
						words = line.split()
						for word in words:
							if word in map:
								total_spam_prob += math.log(float(map.get(word)[1]))
								total_ham_prob += math.log(float(map.get(word)[2]))
				
				prob_spam = prior_spam + total_spam_prob
				prob_ham = prior_ham + total_ham_prob

				if (prob_spam > prob_ham):
						count_spam+=1
						#print("SPAM" + fname)
						if (fname.endswith("spam.txt")):
							 true_positive+=1
						elif (fname.endswith("ham.txt")):
							False_positive+=1

				else:
						count_ham+=1
						if(fname.endswith("spam.txt")):
							print(fname)
						#print("HAM" +fname)
						if (fname.endswith("spam.txt")):
							True_Negative+=1
						elif (fname.endswith("ham.txt")):
							False_Negative+=1
	print(count_ham)
	print(count_spam)
		#print(True_Negative)
	#recall= true_positive/(true_positive+False_Negative)
	#precision=  true_positive/(true_positive+False_positive)
	#F_Score=2*precision*recall/(precision+recall)

if __name__=="__main__":
	classifier(sys.argv[1]);




