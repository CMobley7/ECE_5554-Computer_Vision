# from energy_image import energy_image
# from scipy.misc import imread

def find_greedy_horizontal_seam(energyImage):
    import numpy as np

    nth_row, nth_column = energyImage.shape[0], energyImage.shape[1]
    horizontalSeam = np.zeros((nth_column, 1))
    horizontalSeam[0] = np.argmin(energyImage[:,0])

    for ith_column in xrange(1, nth_column):
        idx = xrange(int(max(horizontalSeam[ith_column - 1] - 1, 0)), int(min(horizontalSeam[ith_column - 1] + 1,nth_row - 1) + 1))
        if horizontalSeam[ith_column - 1] == 0:
            horizontalSeam[ith_column] = horizontalSeam[ith_column - 1] + np.argmin(energyImage[idx, ith_column])
        else:
            horizontalSeam[ith_column] = horizontalSeam[ith_column - 1] + np.argmin(energyImage[idx, ith_column]) - 1
    return horizontalSeam

# print find_greedy_horizontal_seam(energy_image(imread('inputSeamCarvingPrague.jpg')))