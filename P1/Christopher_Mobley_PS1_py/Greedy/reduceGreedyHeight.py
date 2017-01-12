# from energy_image import energy_image
# import matplotlib.pyplot as plot
# from scipy.misc import imread

def reduceGreedyHeight(im, energyImage):
    from find_greedy_horizontal_seam import find_greedy_horizontal_seam
    import numpy as np
    from energy_image import energy_image

    input_color_image = im
    input_image_nth_row, input_image_nth_column, input_image_nth_channel = input_color_image.shape

    reducedColorImage = np.zeros((input_image_nth_row-1,input_image_nth_column,input_image_nth_channel),dtype=np.uint8)

    horizontalSeam = find_greedy_horizontal_seam(energyImage)

    for ith_column in xrange(0, input_image_nth_column):
        reducedColorImage[:,ith_column,0] = np.delete(input_color_image[:,ith_column,0],horizontalSeam[ith_column])
        reducedColorImage[:,ith_column,1] = np.delete(input_color_image[:,ith_column,1],horizontalSeam[ith_column])
        reducedColorImage[:,ith_column,2] = np.delete(input_color_image[:,ith_column,2],horizontalSeam[ith_column])

    reducedEnergyImage = energy_image(reducedColorImage)

    return reducedColorImage,reducedEnergyImage

# reducedColorImage,reducedEnergyImage = reduceGreedyHeight(imread('inputSeamCarvingPrague.jpg'), energy_image(imread('inputSeamCarvingPrague.jpg')))
# plot.subplot(1,2,1)
# plot.imshow(reducedColorImage)
# plot.subplot(1,2,2)
# plot.imshow(reducedEnergyImage)
# plot.show()