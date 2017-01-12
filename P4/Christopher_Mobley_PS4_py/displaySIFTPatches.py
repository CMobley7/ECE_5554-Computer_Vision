import numpy as np


def displaySIFTPatches(positions, scales, orients):

#position is n x 2, scale and orient are n x 1 vectors.
#im is the original image in which the patches were detected.
#This function shows the image with the patches outlined on top of it.

	N = positions.shape[0]

	coners = {}

	for i in range(N):
		row = positions[i,1]
		col = positions[i,0]
		scale = scales[i]
		angle = orients[i]

		magStep = 3
		indexSize = 4
		radius = np.floor(scale*magStep*(indexSize+1)/2)

		tl = np.array([row - radius, col - radius])
		br = np.array([row + radius, col + radius])
		bl = np.array([row + radius, col - radius])
		tr = np.array([row - radius, col + radius])

		rot = np.zeros((2,2))
		rot[0,:] = [np.cos(angle-np.pi/2), np.sin(angle-np.pi/2)]
		rot[1,:] = [-np.sin(angle-np.pi/2), np.cos(angle-np.pi/2)]
		tlr=np.round(np.dot(np.transpose(rot), (tl-np.array([[row],[col]]))) + np.array([[row],[col]]))
		brr=np.round(np.dot(np.transpose(rot), (br-np.array([[row],[col]]))) + np.array([[row],[col]]))
		trr=np.round(np.dot(np.transpose(rot), (tr-np.array([[row],[col]]))) + np.array([[row],[col]]))
		blr=np.round(np.dot(np.transpose(rot), (bl-np.array([[row],[col]]))) + np.array([[row],[col]]))

		coners[i] = [tlr+np.array([[1],[1]]), trr +np.array([[1],[-1]]), brr + np.array([[-1],[-1]]), blr + np.array([[-1],[1]])]

	return coners
