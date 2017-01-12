# from scipy.misc import imread
# import matplotlib.pyplot as plot
# from skimage.draw import circle_perimeter
# import numpy as np

def detectCircles(im, radius, useGradient):
    from skimage.color import rgb2gray
    import skimage
    from skimage.feature import canny
    import numpy as np
    import math
    from imgradient import imgradient

    input_grayscale_image = skimage.img_as_float(rgb2gray(im))

    edges = canny(input_grayscale_image,sigma=3)

    gradient_magnitude, gradient_direction = imgradient(im)

    edges_nth_row, edges_nth_column = edges.shape
    hough_space = np.zeros(edges.shape)

    for ith_row in xrange(0,edges_nth_row):
        for ith_column in xrange(0, edges_nth_column):
            if edges[ith_row,ith_column] == 1:
                if useGradient == 0:
                    for theta in np.arange(0, 2*math.pi,.01):
                        a = int(round(ith_column + radius*math.cos(theta)))
                        b = int(round(ith_row + radius*math.sin(theta)))
                        if a >= 0 and b >= 0 and a < (edges_nth_column - 1) and b < (edges_nth_row - 1):
                            hough_space[b, a] = hough_space[b, a] + 1
                else:
                        theta = gradient_direction[ith_row,ith_column]
                        a = int(round(ith_column + radius*math.cos(theta)))
                        b = int(round(ith_row + radius*math.sin(theta)))
                        if a >= 0 and b >= 0 and a < (edges_nth_column - 1) and b < (edges_nth_row - 1):
                            hough_space[b, a] = hough_space[b, a] + 1

                        theta = gradient_direction[ith_row, ith_column] - math.pi
                        a = int(round(ith_column + radius*math.cos(theta)))
                        b = int(round(ith_row + radius*math.sin(theta)))
                        if a >= 0 and b >= 0 and a < (edges_nth_column - 1) and b < (edges_nth_row - 1):
                            hough_space[b, a] = hough_space[b, a] + 1

    centers_x,centers_y = np.where(hough_space >= .80*np.amax(hough_space))
    centers = np.column_stack((centers_x,centers_y))

    return centers

# centers = detectCircles(imread('jupiter.jpg'),110,0)
#
# input_image = imread('jupiter.jpg')
# for ith_circle in xrange(0,len(centers[:,0])):
#     rr,cc = circle_perimeter(centers[ith_circle,0],centers[ith_circle,1],radius = 110, shape = imread('jupiter.jpg').shape)
#     input_image[rr, cc] = np.array([255,0,0])
#
# plot.imshow(input_image)
# plot.title("Detected circles for jupiter.jpg with radius=110 and useGradient=0")
# plot.show()

