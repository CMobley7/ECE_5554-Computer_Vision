# from energy_image import energy_image
# from cumulative_minimum_energy_map import cumulative_minimum_energy_map
# from scipy.misc import imread

def find_optimal_vertical_seam(cumulativeEnergyMap):
    import numpy as np

    nth_row, nth_column = cumulativeEnergyMap.shape[0], cumulativeEnergyMap.shape[1]
    verticalSeam = np.zeros((nth_row, 1))
    verticalSeam[nth_row - 1] = np.argmin(cumulativeEnergyMap[nth_row - 1,:])

    for ith_row in xrange(nth_row - 2, -1, -1):
        idx = xrange(int(max(verticalSeam[ith_row + 1] - 1, 0)), int(min(verticalSeam[ith_row + 1] + 1,nth_column - 1) + 1))
        if verticalSeam[ith_row + 1] == 0:
            verticalSeam[ith_row] = verticalSeam[ith_row + 1] + np.argmin(cumulativeEnergyMap[ith_row, idx])
        else:
            verticalSeam[ith_row] = verticalSeam[ith_row + 1] + np.argmin(cumulativeEnergyMap[ith_row, idx]) - 1
    return verticalSeam

# print find_optimal_vertical_seam(cumulative_minimum_energy_map(energy_image(imread('inputSeamCarvingPrague.jpg')), 'VERTICAL'))