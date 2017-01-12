import numpy as np

def dist2(x,c):
	ndata, dimx = x.shape
	ncentres, dimc = c.shape
	if dimx != dimc:
		raise NameError('Data dimension does not match dimension of centres')

	n2 = (np.transpose(np.dot(np.ones((ncentres,1)), np.transpose(np.sum(np.square(x),1).reshape(ndata,1)))) +
			np.dot(np.ones((ndata, 1)), np.transpose(np.sum(np.square(c),1).reshape(ncentres,1))) - 
			2 * np.dot(x, np.transpose(c)))

	n2[n2<0] = 0
	return n2