import neurolab
import numpy as np
import neurolab as nl
from parse import *
from max_index import *


def test(pred, predvsactual):
    '''
    Function to test the neural network
    '''
    f = open(pred, "w")
    fp = open(predvsactual, "w")
	output_predicted = []
	correct_predictions = 0
	
	for i in test_input_data:
		val = net.sim([i])[0]
		output_predicted.append(val)
		fp.write(str(val) + "\n")
	print len(test_output_data), "\t", len(output_predicted)

	for i in range(len(test_output_data)):
		predicted = max_index(output_predicted[i])
		actual = max_index(test_output_data[i])
		if predicted == actual:
			correct_predictions += 1
		f.write(str(chr(actual+96)) + "\t\t" + str(chr(predicted + 96)) + "\n")

	accuracy = float(correct_predictions) * 100 / len(test_output_data)
	f.write("\nTotal no. of predictions = " + str(len(test_output_data)))
	f.write("\nCorrect predictions = " + str(correct_predictions))
	f.write("\nAccuracy = " + str(accuracy) + " %\n")
	
	fp.close()
	f.close()


if __name__ == "__main__":
    '''
    Create a feed-forward neural network with
        - hidden layer of size 24
        - output layer of size 26 (one neuron for every letter in the English alphabet)
    Transfer functions of hidden layers are Sigmoid and Softmax respectively
    '''
    li = []
    for i in range(128):
        li.append([0, 1])
    net = nl.net.newff( li , [24, 26], transf = [nl.trans.TanSig(), nl.trans.SoftMax()])
    nl.tool.save(net,'model_24_3000_2400.txt')
    err = net.train(train_input_data, train_output_data ,show=15)

    predictions_file = "predictions.txt"
    predvsactual_file = "predvsactual.txt"
    test(predictions_file, predvsactual_file)
