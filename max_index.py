def max_index(l):
    '''
    Function that returns index of list element with maximum value
    '''
	i = 0
	d = {}
	for item in l:
		d[i] = item
		i += 1
	return sorted(d.items(), key = lambda x : x[1], reverse = True)[0][0] + 1
	
