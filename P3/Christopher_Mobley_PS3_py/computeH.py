import numpy as np
from numpy.linalg import eig

def computeH(t1, t2):

    t1 = np.append(t1,np.ones((1, t1.shape[1])),axis=0)
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

    H = computeH(np.load('points1.npy'),np.load('points2.npy'))
    wdc1 = np.load('points1.npy')
    wdc1 = np.append(wdc1, np.ones((1, wdc1.shape[1])), axis=0)
    normalized_wdc2_calculated = np.dot(H, wdc1)
    wdc2_calculated = np.zeros((normalized_wdc2_calculated.shape[0]-1,normalized_wdc2_calculated.shape[1]))
    wdc2_calculated[0,:] = normalized_wdc2_calculated[0,:]/normalized_wdc2_calculated[2,:]
    wdc2_calculated[1,:] = normalized_wdc2_calculated[1,:]/normalized_wdc2_calculated[2,:]
    print "Calculated pixel:"
    print wdc2_calculated
    print "Original pixel:"
    wdc2 = np.load('points2.npy')
    print wdc2
    reference_image_figure = plot.figure(1)
    reference_image_axis = reference_image_figure.add_subplot(1, 1, 1)
    reference_image_axis.imshow(imread('wdc2.jpg'))
    reference_image_axis.plot(wdc2[0,:],wdc2[1,:],'bo', label='Original')
    reference_image_axis.plot(wdc2_calculated[0,:],wdc2_calculated[1,:],'ro', label='Calculated')
    reference_image_axis.set_title("Reference Image with Original and Homography Calculated Points")
    reference_image_axis.legend(numpoints=1)
    plot.show()
    
    H = computeH(np.transpose(np.load('cc1.npy')),np.transpose(np.load('cc2.npy')))
    cc1 = np.transpose(np.load('cc1.npy'))
    cc1 = np.append(cc1, np.ones((1, cc1.shape[1])), axis=0)
    normalized_cc2_calculated = np.dot(H, cc1)
    cc2_calculated = np.zeros((normalized_cc2_calculated.shape[0]-1,normalized_cc2_calculated.shape[1]))
    cc2_calculated[0,:] = normalized_cc2_calculated[0,:]/normalized_cc2_calculated[2,:]
    cc2_calculated[1,:] = normalized_cc2_calculated[1,:]/normalized_cc2_calculated[2,:]
    print "Calculated C2:"
    print cc2_calculated
    print "Original C2:"
    cc2 = np.transpose(np.load('cc2.npy'))
    print cc2
    reference_image_figure = plot.figure(1)
    reference_image_axis = reference_image_figure.add_subplot(1, 1, 1)
    reference_image_axis.imshow(imread('crop2.jpg'))
    reference_image_axis.plot(cc2[0,:],cc2[1,:],'bo', label='Original')
    reference_image_axis.plot(cc2_calculated[0,:],cc2_calculated[1,:],'ro', label='Calculated')
    reference_image_axis.set_title("Reference Image with Original and Homography Calculated Points")
    reference_image_axis.legend(numpoints=1)
    plot.show()
