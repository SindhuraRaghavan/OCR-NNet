import matplotlib.pyplot as plt
from parse import *
import numpy as np
import PIL


def visualize(img):
    '''
    Function to visualize image using matplotlib image show function
    '''
    plt.imshow(img)
	plt.show()
	return

for i in train_input_data:
	m = 0
	n = 8
	img = []
	for j in range(16):
		img.append(i[m:n])
		m += 8
		n += 8
	visualize(img)
