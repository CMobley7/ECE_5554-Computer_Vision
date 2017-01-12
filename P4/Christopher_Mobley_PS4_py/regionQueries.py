import numpy as np
import scipy.io
import matplotlib.pyplot as plot
from selectRegion import roipoly
from dist2 import dist2
import glob
from scipy.misc import imread, imsave

def region_queries(chosen_frames, km_cluster_centers, k):

    #specify frame directory
    frames_directory = 'frames/'

    #initilize necessary variables
    region_hist = np.zeros((k,), dtype=np.int64)

    #create histogram for chosen frames
    for ith_image in xrange(0, chosen_frames.shape[0]):

        #load particular frame
        mat_file = scipy.io.loadmat(chosen_frames[ith_image, 0])

        #select region of interest
        print "Use your mouse to draw a polygon, right click to end"
        image_name = frames_directory + chosen_frames[ith_image, 0][5:-4]
        image = imread(image_name)
        imsave("query_image_" + str(ith_image) + "_" + str(chosen_frames[ith_image, 0][5:-9]) + ".png", image)

        plot.imshow(image)
        region_of_interest = roipoly(roicolor='r')
        indicies = region_of_interest.getIdx(image, mat_file['positions'])

        #applicable features
        chosen_features = mat_file['descriptors'][indicies,:]

        #compute distances between choosen features and kmeans cluster centers
        distance_between_features = dist2(chosen_features,km_cluster_centers)
        nth_row, _ = distance_between_features.shape

        closest_match = np.zeros((nth_row, 1), dtype=np.int64)

        #determine closest kmeans cluster centers to each feature
        for ith_row in xrange(0,nth_row):
            closest_match[ith_row, 0] = np.argmin(distance_between_features[ith_row])

        hist, _ = np.histogram(closest_match, bins=k)
        region_hist = region_hist + hist

    #normalize histogram
    region_hist = region_hist/chosen_frames.shape[0]
    return region_hist

if __name__ == "__main__":

    #specify sift directory
    sift_directory = 'sift/'
    frames_directory = 'frames/'

    #Get a list of all the .mat file in specified directory.
    frame_names = glob.glob(sift_directory + '*.mat')
    frame_names = [i[-27:] for i in frame_names]

    chosen_frames = np.array([[1957],[1960],[1984],[1990]])
    chosen_frames = np.array([[sift_directory + frame_names[chosen_frames[0,0]-61]],[sift_directory + frame_names[chosen_frames[1,0]-61]], [sift_directory + frame_names[chosen_frames[2,0]-61]], [sift_directory + frame_names[chosen_frames[3,0]-61]]])

    #calculate region histogram
    region_hist = region_queries(chosen_frames, np.load("km_cluster_centers.npy"), 1500)
    np.save("region_hist.npy", region_hist)

    #load necessary files
    # region_hist = np.load("region_hist.npy")
    bag_of_words_histogram = np.load("bag_of_words_histogram.npy")
    map_file_array = np.load("map_file_array.npy")


    #initilize variables
    nth_row, nth_column = bag_of_words_histogram.shape
    simularity_scores = np.empty((1,1))

    # #set bag of words histogram equal to zero where region_hist is equal to zero (should improve accuracy, but doesn't)
    # indices = np.where(region_hist==0)
    #
    # for ith_row in xrange(0, nth_row):
    #     bag_of_words_histogram[ith_row, indices] = 0

    for ith_image in xrange(0,nth_row):
        numerator = (np.dot(bag_of_words_histogram[ith_image,:], region_hist))
        denominator = ((np.linalg.norm(bag_of_words_histogram[ith_image,:]) * np.linalg.norm(region_hist)))
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

    sorted_simularity_scores = simularity_scores.T[sorted_score_index]
    print sorted_simularity_scores
    sorted_map_file_array = map_file_array[sorted_score_index]

    #return image and top 5 closest matches
    for ith_image in xrange(0,6):
        #read the associated image
        image_name = frames_directory + sorted_map_file_array[ith_image,0,0][5:-4]
        print image_name
        image = imread(image_name)
        imsave("closest_match_" + str(ith_image) + "_" + str(image_name[7:-5]) + ".png", image)