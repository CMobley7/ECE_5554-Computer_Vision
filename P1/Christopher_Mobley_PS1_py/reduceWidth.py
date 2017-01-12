# from energy_image import energy_image
# import matplotlib.pyplot as plot
# from scipy.misc import imread

def reduceWidth(im, energyImage):
    from cumulative_minimum_energy_map import cumulative_minimum_energy_map
    from find_optimal_vertical_seam import find_optimal_vertical_seam
    import numpy as np
    from energy_image import energy_image

    input_color_image = im
    input_image_nth_row, input_image_nth_column, input_image_nth_channel = input_color_image.shape

    reducedColorImage = np.zeros((input_image_nth_row,input_image_nth_column-1,input_image_nth_channel),dtype=np.uint8)

    verticalSeam = find_optimal_vertical_seam(cumulative_minimum_energy_map(energyImage, 'VERTICAL'))

    for ith_row in xrange(0, input_image_nth_row):
        reducedColorImage[ith_row,:,0] = np.delete(input_color_image[ith_row,:,0],verticalSeam[ith_row])
        reducedColorImage[ith_row,:,1] = np.delete(input_color_image[ith_row,:,1],verticalSeam[ith_row])
        reducedColorImage[ith_row,:,2] = np.delete(input_color_image[ith_row,:,2],verticalSeam[ith_row])

    reducedEnergyImage = energy_image(reducedColorImage)

    return reducedColorImage,reducedEnergyImage

# reducedColorImage,reducedEnergyImage = reduceWidth(imread('inputSeamCarvingPrague.jpg'), energy_image(imread('inputSeamCarvingPrague.jpg')))
# plot.subplot(1,2,1)
# plot.imshow(reducedColorImage)
# plot.subplot(1,2,2)
# plot.imshow(reducedEnergyImage)
# plot.show()