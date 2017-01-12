import numpy as np
import matplotlib.path as mplPath
import pdb
import matplotlib.pyplot as plt
def getPatchFromSIFTParameters(position, scale, orient, im):

        #position is 2d vector, scale and orient are scalars;
        #im is the image from which the patch will be grabbed.
        #returns in 'patch' the rotated patch from the original image,
        #corresponding to the ROI defined by the SIFT keypoint.

	ny, nx = np.shape(im)

	row = position[1]
	col = position[0]
	angle = orient

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

	tlr=np.round(np.dot(np.transpose(rot), (tl-np.array([[row],[col]]))) + np.array([[row],[col]])) + np.array([[1],[1]])
	trr=np.round(np.dot(np.transpose(rot), (tr-np.array([[row],[col]]))) + np.array([[row],[col]])) + np.array([[1],[-1]])
	brr=np.round(np.dot(np.transpose(rot), (br-np.array([[row],[col]]))) + np.array([[row],[col]])) + np.array([[-1],[-1]])
	blr=np.round(np.dot(np.transpose(rot), (bl-np.array([[row],[col]]))) + np.array([[row],[col]])) + np.array([[-1],[1]])



	# create a mask
	poly_verts = []

	poly_verts.append((tlr[0][0], tlr[1][0]))
	poly_verts.append((trr[0][0], trr[1][0]))
	poly_verts.append((brr[0][0], brr[1][0]))
	poly_verts.append((blr[0][0], blr[1][0]))

	x, y = np.meshgrid(np.arange(nx), np.arange(ny))
	x, y = x.flatten(), y.flatten()

	points = np.vstack((y, x)).T
	
	ROIpath = mplPath.Path(poly_verts)
   	grid = ROIpath.contains_points(points).reshape((ny,nx))

	y_loc = [m[0] for m in poly_verts]
	x_loc = [m[1] for m in poly_verts]

	xmin, xmax = np.min(x_loc), np.max(x_loc)
	ymin, ymax = np.min(y_loc), np.max(y_loc)

	xmin = np.max([xmin, 0])
	xmax = np.min([xmax, im.shape[1]])
	ymin = np.max([ymin, 0])
	ymax = np.min([ymax, im.shape[0]])

	grid = grid[ymin:ymax, xmin:xmax]
	im = im[ymin:ymax, xmin:xmax]



	trimmed = np.ma.masked_array(im, ~grid)
	return trimmed
