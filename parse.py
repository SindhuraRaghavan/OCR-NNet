INPUT_FILE = 'letter.data'

#d = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

def parse_input(total_size, training_size):
    '''
    Function that parses input file and splits it into:
        - Training data 
        - Testing data
    '''
	f = open(INPUT_FILE, 'r')
	bitmap = []
	letter = []
	
	for i in (f.readlines())[3000 : total_size + 3000]:
		i = i.strip()
		line = i.split('\t')
		bitmap.append([int(j) for j in line[6:]])
		l = [0] * 26
		l[ord(line[1]) - 97] = 1
		letter.append(l)
	train_input_data = bitmap[:training_size]
	train_output_data = letter[:training_size]
	test_input_data = bitmap[training_size:]
	test_output_data = letter[training_size:]
	f.close()	
	return train_input_data, train_output_data, test_input_data, test_output_data

train_input_data, train_output_data, test_input_data, test_output_data = parse_input(1000,200)
