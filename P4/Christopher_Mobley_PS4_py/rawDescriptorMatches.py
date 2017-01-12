import numpy as np
import scipy.io
import matplotlib.pyplot as plot
from displaySIFTPatches import displaySIFTPatches
from selectRegion import roipoly
from dist2 import dist2

def raw_descriptor_matches(file_name):

    mat_file = scipy.io.loadmat(file_name)

    print "Use your mouse to draw a polygon, right click to end"
    plot.imshow(mat_file['im1'])
    region_of_interest = roipoly(roicolor='r')
    indicies = region_of_interest.getIdx(mat_file['im1'], mat_file['positions1'])

    chosen_features = mat_file['descriptors1'][indicies,:]

    distance_between_features = dist2(chosen_features,mat_file['descriptors2'])
    nth_row,_ = distance_between_features.shape
    closest_match = np.zeros((1, nth_row),dtype=int)

    for ith_row in xrange(0,nth_row):
        closest_match[0,ith_row] = np.argmin(distance_between_features[ith_row])
    closest_match = closest_match.flatten()
    closest_match = closest_match.tolist()

    corners = displaySIFTPatches(mat_file['positions2'][closest_match,:],mat_file['scales2'][closest_match,:],mat_file['orients2'][closest_match,:])

    return mat_file, region_of_interest, corners

if __name__ == "__main__":
    mat_file, region_of_interest, corners = raw_descriptor_matches('twoFrameData.mat')

    plot.subplot(1,2,1)
    figure_1 = plot.figure(1)
    image_1_axis = figure_1.add_subplot(121)
    image_1_axis.imshow(mat_file['im1'])
    image_1_axis.set_title("Image 1 with Region of Interest")
    region_of_interest.displayROI()

    plot.subplot(1,2,2)
    image_2_axis = figure_1.add_subplot(122)
    image_2_axis.imshow(mat_file['im2'])
    image_2_axis.set_title("Image 2 with Matching Descriptors")

    for j in range(len(corners)):
        image_2_axis.plot([corners[j][0][1], corners[j][1][1]], [corners[j][0][0], corners[j][1][0]], color='g', linestyle='-', linewidth=1)
        image_2_axis.plot([corners[j][1][1], corners[j][2][1]], [corners[j][1][0], corners[j][2][0]], color='g', linestyle='-', linewidth=1)
        image_2_axis.plot([corners[j][2][1], corners[j][3][1]], [corners[j][2][0], corners[j][3][0]], color='g', linestyle='-', linewidth=1)
        image_2_axis.plot([corners[j][3][1], corners[j][0][1]], [corners[j][3][0], corners[j][0][0]], color='g', linestyle='-', linewidth=1)
    image_2_axis.set_xlim(0, mat_file['im2'].shape[1])
    image_2_axis.set_ylim(0, mat_file['im2'].shape[0])
    plot.gca().invert_yaxis()
    plot.show()