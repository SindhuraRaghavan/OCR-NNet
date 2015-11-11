from parse_input import *
from myhmm import *
from max_index import *

model = 'my_model.json' #HMM model
M1 = MyHmmLog(model)    #HMM for vowels
M2 = MyHmmLog(model)    #HMM for consonants

#HMM to train for vowels
M1.forward_backward_multi([tuple(i) for i in v_train_data])

#HMMtrain for consonants
M2.forward_backward_multi([tuple(i) for i in c_train_data])

def test():
    '''
    Test the hybrid model
    Obtain predictions of both HMMs - use this to obtain the one with maximum probability
    '''
    test_data = train_input + test_input
    
    predicted_outputs = []
    for i in range(len(test_data)):
        m1 = M1.forward(tuple(test_data[i]))
        m2 = M2.forward(tuple(test_data[i]))
        predicted = max_index([m1,m2])-1
        predicted_outputs.append(predicted)
    return predicted_outputs

predicted = test()
print "HMM DONE"
