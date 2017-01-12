import matplotlib.pyplot as plot
from matplotlib.widgets import Cursor
import numpy as np

def getting_correspondences(input_image):

    input_image_figure = plot.figure(1)
    input_image_axis = input_image_figure.add_subplot(1, 1, 1)
    input_image_axis.imshow(input_image)
    input_image_axis.set_title("Input Image")
    input_image_cursor = Cursor(input_image_axis, useblit=True, color='red', linewidth=1)

    i = 0
    input_image_correspondences_points = np.empty((2,0))

    try:
        while True:

            i = i + 1

            print "Choose A Feature Point in the Input Image"
            plot.figure(1)
            input_image_correspondences_point = plot.ginput(n = 1, timeout = 0)
            plot.annotate(str(i),(input_image_correspondences_point[0][0],input_image_correspondences_point[0][1]))
            plot.plot(input_image_correspondences_point[0][0], input_image_correspondences_point[0][1], 'ro')
            input_image_correspondences_points = np.hstack((input_image_correspondences_points,np.array([[input_image_correspondences_point[0][0]],[input_image_correspondences_point[0][1]]])))

    except KeyboardInterrupt:
        plot.close("all")
        return input_image_correspondences_points

if __name__ == "__main__":
    from scipy.misc import imread
    input_image_correspondences_points = getting_correspondences(imread('tile1.jpg'))
    np.save("tile1_points.npy", input_image_correspondences_points)
    print input_image_correspondences_points
