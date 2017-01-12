import os
import numpy as np
import matplotlib.pyplot as plot
from computeMHI import computeMHI
from huMoments import huMoments

def showNearestMHIs(testMoments, trainMoments, trainDirectoryNames, K):

    #initilize variables
    distances = np.zeros((1, trainMoments.shape[0]))
    NearestMHIs = np.zeros((480, 640, K+1))

    #reshape testMoments to be a 7x1 array
    testMoments = np.reshape(testMoments,(-1,1))

    #calculate variance
    variance = np.reshape(np.nanvar(trainMoments,axis=0),(-1,1))

    #calculate normalized Euclidean distance between testMoment and each trainMoment
    for ith_train_moment in xrange(0, trainMoments.shape[0]):
        distances[:,ith_train_moment] = np.sqrt(np.sum(np.divide(np.power(np.reshape(trainMoments[ith_train_moment,:],(-1,1))-testMoments,2),variance)))

    #sort distances
    sorted_index = np.argsort(distances)

    #sort trainDirectoryNames
    sorted_train_directory_names = np.reshape(trainDirectoryNames[sorted_index],(trainDirectoryNames.shape))

    #return K closest matches
    for ith_closest_match in xrange(0, K+1):
        NearestMHIs[:,:,ith_closest_match] = computeMHI(sorted_train_directory_names[ith_closest_match,:][0])

    return NearestMHIs

if __name__ == "__main__":

    #initilize variables
    base_directory = './'
    actions = ['botharms', 'crouch', 'leftarmup', 'punch', 'rightkick']
    trainDirectoryNames = []
    trainMoments = np.asarray(np.load('huVectors.npy'))
    K = 4

    #collect all subdirectory names
    for action in actions:
        directory_name = base_directory + action + '/'
        trainDirectoryNames = trainDirectoryNames + [directory_name + subdirectory_name for subdirectory_name in os.listdir(directory_name)]
    trainDirectoryNames = np.reshape(trainDirectoryNames,(-1,1))

    #choose 1st MHI
    chosen_MHI = np.load('botharms-up-p1-1_MHI.npy')
    testMoments = huMoments(chosen_MHI)

    #compute the Kth closest images
    NearestMHIs = showNearestMHIs(testMoments, trainMoments, trainDirectoryNames, K)

    #plot the MHI itself
    figure = plot.figure(frameon=False)
    axis = figure.add_subplot(1, 1, 1)
    axis.imshow(NearestMHIs[:,:,0])
    axis.set_title("Chosen MHI - botharms-up-p1-1_MHI")
    figure.add_axes(axis)
    figure.savefig('Chosen_MHI_botharms-up-p1-1_MHI.png')
    plot.show()

    #show the Kth closest images
    for ith_MHI in xrange(1,K+1):
        figure = plot.figure(ith_MHI)
        axis = figure.add_subplot(1, 1, 1)
        axis.imshow(NearestMHIs[:,:,ith_MHI])
        axis.set_title("Nearest Neighbor " + str(ith_MHI) +" to botharms-up-p1-1 MHI")
        figure.add_axes(axis)
        figure.savefig("Nearest_Neighbor" + str(ith_MHI) + "_MHI_to_botharms-up-p1-1_MHI.png")
        plot.show()

    #choose 2nd MHI
    chosen_MHI = np.load('rightkick-p1-1_MHI.npy')
    testMoments = huMoments(chosen_MHI)

    #compute the Kth closest images
    NearestMHIs = showNearestMHIs(testMoments, trainMoments, trainDirectoryNames, K)

    #plot the MHI itself
    figure = plot.figure(frameon=False)
    axis = figure.add_subplot(1, 1, 1)
    axis.imshow(NearestMHIs[:,:,0])
    axis.set_title("Chosen MHI - rightkick-p1-1_MHI")
    figure.add_axes(axis)
    figure.savefig('Chosen_MHI_rightkick-p1-1_MHI.png')
    plot.show()

    #show the Kth closest images
    for ith_MHI in xrange(1,K+1):
        figure = plot.figure(ith_MHI)
        axis = figure.add_subplot(1, 1, 1)
        axis.imshow(NearestMHIs[:,:,ith_MHI])
        axis.set_title("Nearest Neighbor " + str(ith_MHI) +" to rightkick-p1-1 MHI")
        figure.add_axes(axis)
        figure.savefig("Nearest_Neighbor" + str(ith_MHI) + "_MHI_to_rightkick-p1-1_MHI.png")
        plot.show()