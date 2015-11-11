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

