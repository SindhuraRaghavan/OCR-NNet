import numpy as np
import neurolab as nl
from parse-hybrid import *
from max_index import *


def test(fname):
    f = open(fname, "w")
	output_predicted = []
	correct_predictions = 0
	
	for i in test_input_data:

		val = net.sim([i])[0]
		output_predicted.append(val)
		
	print len(test_output_data), "\t", len(output_predicted)

	for i in range(len(test_output_data)):
		predicted = max_index(output_predicted[i])
		actual = max_index(test_output_data[i])
		if predicted == actual:
			correct_predictions += 1
		f.write(str(actual) + "\t\t" + str(predicted) + "\n")

	accuracy = float(correct_predictions) * 100 / len(test_output_data)

    f.write("\nTotal no. of predictions = " + str(len(test_output_data)))
	f.write("\nCorrect predictions = " + str(correct_predictions))
	f.write("\nAccuracy = " + str(accuracy) + " %\n")
	
	f.close()

if __name__ == "__main__":
    li=[]
    #input is now bitmap 16 x 8 and one binary value indicating vowel/consonant
    for i in range(129): 
	    li.append([0, 1])

    net = nl.net.newff(li , [24, 26], transf = [nl.trans.TanSig(), nl.trans.SoftMax()])

    err = net.train(train_input_data, train_output_data ,show=15)
    fname = "output.txt"
    test(fname)
