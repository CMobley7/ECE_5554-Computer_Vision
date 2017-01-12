# import matplotlib.pyplot as plot
# from energy_image import energy_image
# from scipy.misc import imread, imsave

def cumulative_minimum_energy_map(energyImage, seamDirection):
    import numpy as np

    nth_row, nth_column = energyImage.shape[0], energyImage.shape[1]

    if seamDirection == 'VERTICAL':
        cumulativeEnergyMap = np.zeros(energyImage.shape)
        cumulativeEnergyMap[:1,:] = energyImage[:1,:]
        for ith_row in xrange(1, nth_row):
            for jth_column in xrange(0, nth_column):
                idx = xrange(max(jth_column - 1, 0), min(jth_column + 1, (nth_column - 1)) + 1)
                cumulativeEnergyMap[ith_row ,jth_column] = energyImage[ith_row, jth_column] + min(cumulativeEnergyMap[ith_row - 1, idx])
    elif seamDirection == 'HORIZONTAL':
        cumulativeEnergyMap = np.zeros(energyImage.shape)
        cumulativeEnergyMap[:,:1] = energyImage[:,:1]
        for jth_column in xrange(1, nth_column):
            for ith_row in xrange(0, nth_row):
                idx = xrange(max(ith_row - 1, 0), min(ith_row + 1,(nth_row - 1)) + 1)
                cumulativeEnergyMap[ith_row, jth_column] = energyImage[ith_row, jth_column] + min(cumulativeEnergyMap[idx, jth_column - 1])
    else:
        print("Invalid seamDirection. The valid inputs for seamDirection are HORIZONTAL or VERTICAL.")
    return cumulativeEnergyMap

# cumulativeEnergyMap = cumulative_minimum_energy_map(energy_image(imread('inputSeamCarvingPrague.jpg')), 'VERTICAL')
# imsave('outputCumulativeEnergyMapVertical.png', cumulativeEnergyMap)
# imsave('outputCumulativeEnergyMapVerticalWithRoberts.png', cumulativeEnergyMap)
# plot.imshow(cumulativeEnergyMap)
# plot.show()

# cumulativeEnergyMap = cumulative_minimum_energy_map(energy_image(imread('inputSeamCarvingPrague.jpg')), 'HORIZONTAL')
# imsave('outputCumulativeEnergyMapHorizontal.png', cumulativeEnergyMap)
# imsave('outputCumulativeEnergyMapHorizontalWithRoberts.png', cumulativeEnergyMap)
# plot.imshow(cumulativeEnergyMap)
# plot.show()
