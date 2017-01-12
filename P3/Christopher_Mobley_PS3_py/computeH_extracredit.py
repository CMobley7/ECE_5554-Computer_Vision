import numpy as np
from numpy.linalg import eig

def computeH(t1):

    t1 = np.append(t1,np.ones((1, t1.shape[1])),axis=0)
    t2 = np.array([[0,50,50,0],[0,0,50,50]])
    L = np.zeros((2 * t1.shape[1],9))
    ith_correspondance = 0

    for ith_row in xrange(0, 2 * t1.shape[1], 2):
        L[ith_row] = [t1[0,ith_correspondance], t1[1,ith_correspondance], t1[2, ith_correspondance], 0, 0, 0,
                      -t2[0,ith_correspondance]*t1[0,ith_correspondance], -t2[0,ith_correspondance]*t1[1,ith_correspondance], -t2[0,ith_correspondance]*t1[2,ith_correspondance]]
        L[ith_row + 1] = [0, 0, 0, t1[0,ith_correspondance], t1[1,ith_correspondance], t1[2, ith_correspondance],
                          -t2[1,ith_correspondance]*t1[0,ith_correspondance], -t2[1,ith_correspondance]*t1[1,ith_correspondance], -t2[1,ith_correspondance]*t1[2,ith_correspondance]]
        ith_correspondance = ith_correspondance + 1

    A = np.dot(L.T, L)

    eigenvalues, eigenvectors = eig(A)

    minimum_engenvalue = np.argmin(eigenvalues)

    H = np.reshape(eigenvectors[:,minimum_engenvalue],(3,3))

    return H

if __name__ == "__main__":
    from scipy.misc import imread
    import matplotlib.pyplot as plot
    H = computeH(np.load('tile1_points.npy'))
    tile1 = np.load('tile1_points.npy')
    tile1 = np.append(tile1, np.ones((1, tile1.shape[1])), axis=0)
    normalized_tile2_calculated = np.dot(H, tile1)
    tile2_calculated = np.zeros((normalized_tile2_calculated.shape[0]-1,normalized_tile2_calculated.shape[1]))
    tile2_calculated[0,:] = normalized_tile2_calculated[0,:]/normalized_tile2_calculated[2,:]
    tile2_calculated[1,:] = normalized_tile2_calculated[1,:]/normalized_tile2_calculated[2,:]
    input_image_figure = plot.figure(1)
    input_image_axis = input_image_figure.add_subplot(1, 1, 1)
    input_image_axis.imshow(imread('tile1.jpg'))
    input_image_axis.plot(tile1[0,:],tile1[1,:],'bo', label='Original')
    input_image_axis.plot(tile2_calculated[0,:],tile2_calculated[1,:],'ro', label='Calculated')
    input_image_axis.set_title("Reference Image with Original and Homography Calculated Points")
    input_image_axis.legend(numpoints=1)
    plot.show()

