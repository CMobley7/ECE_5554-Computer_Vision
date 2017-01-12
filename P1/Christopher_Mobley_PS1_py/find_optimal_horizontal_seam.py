# from energy_image import energy_image
# from cumulative_minimum_energy_map import cumulative_minimum_energy_map
# from scipy.misc import imread

def find_optimal_horizontal_seam(cumulativeEnergyMap):
    import numpy as np

    nth_row, nth_column = cumulativeEnergyMap.shape[0], cumulativeEnergyMap.shape[1]
    horizontalSeam = np.zeros((nth_column, 1))
    horizontalSeam[nth_column - 1] = np.argmin(cumulativeEnergyMap[:,nth_column - 1])

    for ith_column in xrange(nth_column - 2, -1, -1):
        idx = xrange(int(max(horizontalSeam[ith_column + 1] - 1, 0)), int(min(horizontalSeam[ith_column + 1] + 1,nth_row - 1) + 1))
        if horizontalSeam[ith_column + 1] == 0:
            horizontalSeam[ith_column] = horizontalSeam[ith_column + 1] + np.argmin(cumulativeEnergyMap[idx, ith_column])
        else:
            horizontalSeam[ith_column] = horizontalSeam[ith_column + 1] + np.argmin(cumulativeEnergyMap[idx, ith_column]) - 1
    return horizontalSeam

# print find_optimal_horizontal_seam(cumulative_minimum_energy_map(energy_image(imread('inputSeamCarvingPrague.jpg')), 'HORIZONTAL'))