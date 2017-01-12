import numpy as np
import scipy.io
import glob
from scipy.misc import imread, imsave
from dist2 import dist2

def full_frame_queries(km_cluster_centers, numbers_of_images, k):

    #specify sift directory
    sift_directory = 'sift/'

    # Get a list of all the .mat file in specified directory.
    frame_names = glob.glob(sift_directory + '*.mat')
    frame_names = [i[-27:] for i in frame_names]

    #initilize necessary variables
    bag_of_words_histogram = np.empty((1,k))
    mat_file_array = np.empty((1,1))

    for i in xrange(0, numbers_of_images):
        print 'reading frame %d of %d' %(i, numbers_of_images - 1)

        # load that file
        frame_name = sift_directory + frame_names[i+1599]
        mat_file = scipy.io.loadmat(frame_name)

        distance_between_features = dist2(mat_file['descriptors'],km_cluster_centers)
        nth_row, _ = distance_between_features.shape

        closest_match = np.zeros((nth_row, 1), dtype=np.int64)

        for ith_row in xrange(0,nth_row):
            closest_match[ith_row, 0] = np.argmin(distance_between_features[ith_row])

        hist, _ = np.histogram(closest_match,bins=k)
        bag_of_words_histogram = np.vstack((bag_of_words_histogram,hist))
        mat_file_array = np.vstack((mat_file_array, frame_name))

    bag_of_words_histogram = bag_of_words_histogram[1:,:]
    map_file_array = mat_file_array[1:,:]
    return bag_of_words_histogram, map_file_array

if __name__ == "__main__":
    #calculate bag of words histogram
    bag_of_words_histogram, map_file_array = full_frame_queries(np.load("km_cluster_centers.npy"), 400, 1500)
    np.save("bag_of_words_histogram.npy", bag_of_words_histogram)
    np.save("map_file_array.npy", map_file_array)

    # bag_of_words_histogram = np.load("bag_of_words_histogram.npy")
    # map_file_array = np.load("map_file_array.npy")

    #specify sift directory
    sift_directory = 'sift/'
    frames_directory = 'frames/'

    #initilize variables
    nth_row, nth_column = bag_of_words_histogram.shape
    query_image = 1834 - 1660 #entry the number of the frame you would like to query about
    query_image_hist = bag_of_words_histogram[query_image,:]
    simularity_scores = np.empty((1,1))

    for ith_image in xrange(0,nth_row):
        numerator = (np.dot(bag_of_words_histogram[ith_image,:], query_image_hist))
        denominator = ((np.linalg.norm(bag_of_words_histogram[ith_image,:]) * np.linalg.norm(query_image_hist)))
        if denominator != 0.0:
            simularity_score = numerator / denominator
            simularity_scores = np.vstack((simularity_scores,[simularity_score]))
        else:
            simularity_score = 0.0
            simularity_scores = np.vstack((simularity_scores,[simularity_score]))

    #remove null row
    simularity_scores = simularity_scores[1:,:].T

    #sort array from greatest to least and return indicies
    sorted_score_index = np.argsort(simularity_scores)
    sorted_score_index = sorted_score_index[:,::-1]
    sorted_score_index = sorted_score_index.T

    sorted_map_file_array = map_file_array[sorted_score_index]

    #return query image
    image_name = frames_directory + map_file_array[query_image,0][5:-4]
    image = imread(image_name)
    imsave("query_image_" + str(query_image + 1660) + ".png", image)

    #return image and top 5 closest matches
    for ith_image in xrange(0,6):
        #read the associated image
        image_name = frames_directory + sorted_map_file_array[ith_image,0,0][5:-4]
        print image_name
        image = imread(image_name)
        imsave("closest_match_" + str(ith_image)+ "_image_" + str(query_image + 1660) +".png", image)