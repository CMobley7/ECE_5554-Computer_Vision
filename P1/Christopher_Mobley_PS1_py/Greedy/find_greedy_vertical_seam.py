# from energy_image import energy_image
# from scipy.misc import imread

def find_greedy_vertical_seam(energyImage):
    import numpy as np

    nth_row, nth_column = energyImage.shape[0], energyImage.shape[1]
    verticalSeam = np.zeros((nth_row, 1))
    verticalSeam[0] = np.argmin(energyImage[0,:])

    for ith_row in xrange(1, nth_row):
        idx = xrange(int(max(verticalSeam[ith_row - 1] - 1, 0)), int(min(verticalSeam[ith_row - 1] + 1,nth_column - 1) + 1))
        if verticalSeam[ith_row - 1] == 0:
            verticalSeam[ith_row] = verticalSeam[ith_row - 1] + np.argmin(energyImage[ith_row, idx])
        else:
            verticalSeam[ith_row] = verticalSeam[ith_row - 1] + np.argmin(energyImage[ith_row, idx]) - 1
    return verticalSeam

# print find_greedy_vertical_seam(energy_image(imread('inputSeamCarvingPrague.jpg')))