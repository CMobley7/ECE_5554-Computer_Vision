import os
import glob
import numpy as np
from scipy.misc import imread
import matplotlib.pyplot as plot



def computeMHI(directoryName):

    #load frames in specified directory
    depthfiles = glob.glob(directoryName + '/' '*.pgm')
    depthfiles = np.sort(depthfiles)

    #initlize variables
    tau = len(depthfiles)
    threshold = 39000
    motion_history_image = np.zeros((imread(depthfiles[0]).shape[0], imread(depthfiles[0]).shape[1]))

    #loop through each frame
    for ith_image in xrange(0, tau):
        # #state which image out of how many is being read
        # print str(ith_image + 1) +" out of " + str(tau) +":"

        #read depth image
        depth_image = imread(depthfiles[ith_image])

        #threshold depth image
        depth_image[depth_image > threshold] = 0
        depth_image[depth_image != 0] = 1

        #compute motion history image
        if ith_image > 0:
            #calculate difference image
            difference_image = np.absolute(depth_image - pervious_image)

            #most efficient way
            motion_history_image[difference_image == 1] = tau
            motion_history_image[difference_image != 1] = motion_history_image[difference_image != 1] - 1
            motion_history_image[motion_history_image < 0] = 0

            # #efficient way
            # indicies_tau = np.where(difference_image == 1)
            # indicies_otherwise = np.where(difference_image != 1)
            # motion_history_image[indicies_tau] = tau
            # motion_history_image[indicies_otherwise] = motion_history_image[indicies_otherwise] - 1
            # motion_history_image[motion_history_image < 0] = 0

            # #inefficient way
            # for ith_row in xrange(0, motion_history_image.shape[0]):
            #     for ith_column in xrange(0,motion_history_image.shape[1]):
            #         if np.absolute(depth_image[ith_row,ith_column] - pervious_image[ith_row,ith_column]) == 1:
            #             motion_history_image[ith_row,ith_column] = tau
            #         else:
            #             motion_history_image[ith_row,ith_column] = max(0, motion_history_image[ith_row,ith_column] - 1)

            pervious_image = depth_image
        else:
            pervious_image = depth_image

    motion_history_image = motion_history_image/np.amax(motion_history_image)

    return motion_history_image

if __name__ == "__main__":

    #Save three images
    motion_history_image = computeMHI('./botharms/botharms-up-p1-1')
    figure = plot.figure(frameon=False)
    axis = figure.add_subplot(1,1,1)
    axis.imshow(motion_history_image)
    axis.set_title('Both Arms')
    figure.add_axes(axis)
    figure.savefig('botharms-up-p1-1_MHI.png')
    np.save('botharms-up-p1-1_MHI.npy', motion_history_image)


    motion_history_image = computeMHI('./crouch/crouch-p1-1')
    figure = plot.figure(frameon=False)
    axis = figure.add_subplot(1,1,1)
    axis.imshow(motion_history_image)
    axis.set_title('Crouch')
    figure.add_axes(axis)
    figure.savefig('crouch-p1-1_MHI.png')
    np.save('crouch-p1-1_MHI.npy', motion_history_image)

    motion_history_image = computeMHI('./rightkick/rightkick-p1-1')
    figure = plot.figure(frameon=False)
    axis = figure.add_subplot(1,1,1)
    axis.imshow(motion_history_image)
    axis.set_title('Right Kick')
    figure.add_axes(axis)
    figure.savefig('rightkick-p1-1_MHI.png')
    np.save('rightkick-p1-1_MHI.npy', motion_history_image)

    #MHIs of all sequences
    #initilize variables
    base_directory = './'
    actions = ['botharms', 'crouch', 'leftarmup', 'punch', 'rightkick']
    directoryNames = []
    motion_history_image = np.zeros((480, 640, 20))
    #collect all subdirectory names
    for action in actions:
        directory_name = base_directory + action + '/'
        directoryNames = directoryNames + [directory_name + subdirectory_name for subdirectory_name in os.listdir(directory_name)]

    #loop through each subdirectory
    for ith_directory in xrange(0, len(directoryNames)):
        motion_history_image[:,:,ith_directory] = computeMHI(directoryNames[ith_directory])
    np.save('allMHIs.npy',motion_history_image)
    # # #Time program runtime
    # # from timeit import Timer
    # # timer = Timer("computeMHI('botharms')","from computeMHI import computeMHI")
    # # print timer.timeit(1)