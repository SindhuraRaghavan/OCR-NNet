#Optical Character Recognition using Neural Network

In this exercise, we use [Neurolab](https://pypi.python.org/pypi/neurolab) to build an Optical Character Recognition System.

Neurolab is a simple and powerful Neural Network library in Python containing neural network training algorithms and frameworks for different neural networks.

###Dataset 
```
Dataset : letter.data
* Every entry in dataset is of the format
        - id
        - letter
        - next_id
        - word_id
        - position
        - fold
        - bitmap image for each letter of size 16 x 8 (128 binary values)
* Dataset size = 52152
* Training size = 800
* Testing size = 200
* We can visualize the input data as an image using matplotlib
```
###Neural Network
``` 
A feed-forward neural network is used with architecture : 
  1. Input layer
     - size 128 (representing bitmap of the character)
  2. Hidden layer 
     - size 24 
     - Tangent sigmoid transfer function
  3. Output layer (can be Softmax or Logistical Regression layer)
     - size 26 (one neuron for every alphabet) 
     - Softmax transfer function 

NOTE :
* If we use Softmax output layer, output neurons are a probability distribution across the 26 letters and the predicted alphabet is the one with maximum probability
* If output is Logistic Regression based, then output layer represents a one-hot vector of size 26 (1 for the target character, 0 for the others)
  ex : The letter 'c' is represented as the one-hot vector
       [ 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ]
```
###Testing Results
```
Format of the output recording are:
 * Output File
 * Size of Train data
 * Size of Test data
 * Size of hidden layer
 * Accuracy

Accuracies obtained with various config params of the Neural Network are:

output_16.txt - 800 - 200 - 16 - 68.5%
output_16(1).txt - 800 -200 - 16 - 78%
output_16.txt - 2400 - 600 - 16 - 74.83%

output_24.txt - 800 - 200 - 24 - 73.0%
output_32.txt - 800 - 200 - 32 - 73.5%
output_48.txt - 800 - 200 - 48 - 79.5%

output_16_16.txt - 800 - 200 - 16 - 16 - 73.0%
output_24_16.txt - 800 - 200 - 24 - 16 - 70.0%

Inference:
 * We observed that increasing number of neurons in hidden layer and increasing number of hidden layers can increase accuracy but this increase in accuracy stagnates after a threshold of these parameters.
 * As we increase size of training data, we obtain better accuracy.
 * The maximum accuracy we obtained was of 79.5% with 48 neurons in the single hidden layer.
```
##VARIATIONS
```
Hybrid model of OCR with HMM and Neural Networks:
In this approach, we build a train a HMM classifier to obtain metadata about the input character (16 x 8 bitmap) as either vowel or consonant.

HMM implementation used is myhmm.py (https://github.com/ananthpn/pyhmm.git)

Variation 1 :
* Build a HMM classifier trained on whether the character is a vowel or consonant
* For test data, predict whether the character is a vowel or not
* Give this as input to neural network along with the bitmap of the character
* Hence, now the input layer size is 129

Variation 2 :
* Take all pairs of input data to give 2 x 128 = 256 element vector (character pairs)
* Label (Target labels to be predicted) every character pair as
    + vowel - vowel (v-v)
    + vowel - consonant (v-c)
    + consonant - vowel (c-v)
    + consonant - consonant (c-c)
* Divide the dataset into 4 banks of data based on the above. 
  Split these into train and test subsets of a sample of 3:2 ratio 
* Now, we train HMMs on each of these data banks using the Forward-Backward/Baum Welch algorithm
* Each of these HMMs thus recognizes whether the character pair is a v-v, v-c, c-v or c-c sequence
* Take the test data and predict the sequence for each HMM to obtain 4 probabilities. 
  The maximum of these gives the correct sequence and hence the correct 2 bits of metadata
* Feed the character pair bitmap along with the HMM predicted 2 bit sequence to the 
  neural network as input with target (output layer neurons) being the character's one-hot vector


Why these variations?
* These variations provide more information to the Neural Network and help improve it's performance
* Consider the example : The bitmap representation of 'a' and 'd' are similar and hence hard to differentiate for the system. 
  With 2 bits of metadata to train the system to recognize vowel-consonant sequence pairs helps resolve this issue fairly.

Performance of the hybrid OCR system:
+ output_16_best.txt	- best accuracy of 79.5% with 16 hidden units and 800 training and 200 test data
+ output_16_1.txt		- accuracy of 76.5% with 16 hidden units and 800 training and 200 test data
Clearly, the hybrid OCR system performs better than the Neural Network based OCR
``` 
