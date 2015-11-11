INPUT_FILE='letter.data'
from Hmm import *
#d = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

def parse_input():
	f=open(INPUT_FILE,'r')
	bitmap=[]
	letter=[]
	k = 0
	for i in (f.readlines())[0:1000]:
		i=i.strip()
		line=i.split('\t')
		b=[int(j) for j in line[6:]]
		b.append(predicted[k])
		bitmap.append(b)
		l=[0]*26
		l[ord(line[1])-97]=1
		letter.append(l)
		k+=1
	train_input_data=bitmap[:800]
	train_output_data=letter[:800]
	test_input_data=bitmap[800:]
	test_output_data=letter[800:]
	f.close()	
	return train_input_data,train_output_data,test_input_data,test_output_data

print "PARSE DONE"
train_input_data,train_output_data,test_input_data,test_output_data=parse_input()
