import numpy as np
import scipy.io
import glob
from sklearn.cluster import KMeans
from scipy.misc import imread, imsave
from getPatchFromSIFTParameters import getPatchFromSIFTParameters
from skimage.color import rgb2gray

def visualize_vocabulary(numbers_of_images, k):

    #initilize variables
    dataset = np.empty((1,128), dtype=np.float64)
    lookup_information = np.empty((1,2), dtype=np.object)

    #specify sift directory
    sift_directory = 'sift/'

    # Get a list of all the .mat file in specified directory.
    frame_names = glob.glob(sift_directory + '*.mat')
    frame_names = [i[-27:] for i in frame_names]

    for i in xrange(0, numbers_of_images):
        print 'reading frame %d of %d' %(i, numbers_of_images - 1)

        # load that file
        frame_name = sift_directory + frame_names[i]
        mat_file = scipy.io.loadmat(frame_name)

        #create dataset and lookup information for each sift descriptor
        dataset = np.vstack((dataset, mat_file['descriptors']))
        mat_file_name = np.empty((mat_file['descriptors'].shape[0],1),dtype=object)
        mat_file_name[:] = frame_name
        number_of_features = np.ones((mat_file['descriptors'].shape[0],1),dtype=object) * mat_file['descriptors'].shape[0]
        lookup_information = np.vstack((lookup_information,np.hstack((mat_file_name,number_of_features + lookup_information.shape[0] - 1))))

    #delect empty row
    dataset = dataset[1:,:]
    lookup_information = lookup_information[1:,:]

    #cluster data by k
    km = KMeans(n_clusters = k)
    km.fit(dataset)
    km_cluster_centers = km.cluster_centers_
    km_descriptor_labels = np.reshape(km.labels_,(km.labels_.shape[0],1))

    #build lookup array
    visual_vocabulary = np.hstack((km_descriptor_labels,lookup_information))

    return visual_vocabulary, km_descriptor_labels, km_cluster_centers


if __name__ == "__main__":
#     visual_vocabulary, km_descriptor_labels, km_cluster_centers = visualize_vocabulary(300, 1500)
#
#     #save files for later use
#     np.save("visual_vocabulary.npy", visual_vocabulary)
#     np.save("km_descriptor_labels.npy", km_descriptor_labels)
#     np.save("km_cluster_centers.npy", km_cluster_centers)

    #load necessary variables
    visual_vocabulary = np.load("visual_vocabulary.npy")
    km_descriptor_labels = np.load("km_descriptor_labels.npy")
    km_cluster_centers = np.load("km_cluster_centers.npy")

    #specify sift directory
    sift_directory = 'sift/'
    frames_directory = 'frames/'

    #initilize necessary variables
    nth_row, nth_column = visual_vocabulary.shape
    number_of_patches = 0
    desired_number_of_patches = 25
    label = 3

    #retrieve 25 patches similiar to label
    print "retrieving 25 patches similiar to label " + str(label)
    for ith_row in xrange(0, nth_row):
        if number_of_patches < desired_number_of_patches:
            if visual_vocabulary[ith_row, 0] == label:
                mat_file = scipy.io.loadmat(visual_vocabulary[ith_row, 1])
                image_name = frames_directory + visual_vocabulary[ith_row, 1][5:-4]
                image = imread(image_name)
                current_row = ith_row - (visual_vocabulary[ith_row, 2] - mat_file['descriptors'].shape[0])
                image_patch = getPatchFromSIFTParameters(mat_file['positions'][current_row,:],mat_file['scales'][current_row],mat_file['orients'][current_row],rgb2gray(image))
                imsave('patch_' + str(number_of_patches) + "_" + str(label) + ".png",image_patch)
                number_of_patches = number_of_patches + 1
                print "patch number: " + str(number_of_patches) + " for label " + str(label)
            else:
                pass
        else:
            break

    #reinitilize number of patches and label variables
    number_of_patches = 0
    label = 1492

    #retrieve 25 patches similiar to label
    print "retrieving 25 patches similiar to label " + str(label)
    for ith_row in xrange(0, nth_row):
        if number_of_patches < desired_number_of_patches:
            if visual_vocabulary[ith_row, 0] == label:
                mat_file = scipy.io.loadmat(visual_vocabulary[ith_row, 1])
                image_name = frames_directory + visual_vocabulary[ith_row, 1][5:-4]
                image = imread(image_name)
                current_row = ith_row - (visual_vocabulary[ith_row, 2] - mat_file['descriptors'].shape[0])
                image_patch = getPatchFromSIFTParameters(mat_file['positions'][current_row,:],mat_file['scales'][current_row],mat_file['orients'][current_row],rgb2gray(image))
                imsave('patch_' + str(number_of_patches) + "_" + str(label) + ".png",image_patch)
                number_of_patches = number_of_patches + 1
                print "patch number: " + str(number_of_patches) + " for label " + str(label)
            else:
                pass
        else:
            break

