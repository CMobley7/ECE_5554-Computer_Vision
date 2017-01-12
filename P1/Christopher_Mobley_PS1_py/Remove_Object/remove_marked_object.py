# from scipy.misc import imsave, imread
# import matplotlib.pyplot as plot

def reduceWidth(im, energyImage):
    from cumulative_minimum_energy_map import cumulative_minimum_energy_map
    from find_optimal_vertical_seam import find_optimal_vertical_seam
    import numpy as np

    input_color_image = im
    input_image_nth_row, input_image_nth_column, input_image_nth_channel = input_color_image.shape
    energyImage_nth_row, energyImage_nth_column = energyImage.shape[0],energyImage.shape[1]

    reducedColorImage = np.zeros((input_image_nth_row, input_image_nth_column-1,input_image_nth_channel),dtype=np.uint8)
    reducedEnergyImage = np.zeros((energyImage_nth_row, energyImage_nth_column-1))

    verticalSeam = find_optimal_vertical_seam(cumulative_minimum_energy_map(energyImage, 'VERTICAL'))

    for ith_row in xrange(0, input_image_nth_row):
        reducedColorImage[ith_row,:,0] = np.delete(input_color_image[ith_row,:,0],verticalSeam[ith_row])
        reducedColorImage[ith_row,:,1] = np.delete(input_color_image[ith_row,:,1],verticalSeam[ith_row])
        reducedColorImage[ith_row,:,2] = np.delete(input_color_image[ith_row,:,2],verticalSeam[ith_row])
        reducedEnergyImage[ith_row,:] = np.delete(energyImage[ith_row,:],verticalSeam[ith_row])

    return reducedColorImage,reducedEnergyImage

def reduceHeight(im, energyImage):
    from cumulative_minimum_energy_map import cumulative_minimum_energy_map
    from find_optimal_horizontal_seam import find_optimal_horizontal_seam
    import numpy as np

    input_color_image = im
    input_image_nth_row, input_image_nth_column, input_image_nth_channel = input_color_image.shape
    energyImage_nth_row, energyImage_nth_column = energyImage.shape[0],energyImage.shape[1]

    reducedColorImage = np.zeros((input_image_nth_row-1,input_image_nth_column,input_image_nth_channel),dtype=np.uint8)
    reducedEnergyImage = np.zeros((energyImage_nth_row-1,energyImage_nth_column))

    horizontalSeam = find_optimal_horizontal_seam(cumulative_minimum_energy_map(energyImage, 'HORIZONTAL'))

    for ith_column in xrange(0, input_image_nth_column):
        reducedColorImage[:,ith_column,0] = np.delete(input_color_image[:,ith_column,0],horizontalSeam[ith_column])
        reducedColorImage[:,ith_column,1] = np.delete(input_color_image[:,ith_column,1],horizontalSeam[ith_column])
        reducedColorImage[:,ith_column,2] = np.delete(input_color_image[:,ith_column,2],horizontalSeam[ith_column])
        reducedEnergyImage[:,ith_column] = np.delete(energyImage[:,ith_column],horizontalSeam[ith_column])

    return reducedColorImage,reducedEnergyImage


def removed_marked_object(im,desired_reduction_width, desired_reduction_height):
    from scipy.misc import imread
    from energy_image import energy_image
    from mark_object import mark_object

    input_color_image = imread(im)
    input_energy_image = energy_image(input_color_image)
    reduced_energy_image = mark_object(input_color_image,input_energy_image)
    reduced_color_image = input_color_image


    for ith_pixel in xrange(0, desired_reduction_width):
        reduced_color_image,reduced_energy_image = reduceWidth(reduced_color_image,reduced_energy_image)
        print str(ith_pixel+1) + " pixel removed"

    for ith_pixel in xrange(0, desired_reduction_height):
        reduced_color_image,reduced_energy_image = reduceHeight(reduced_color_image,reduced_energy_image)
        print str(ith_pixel+1) + " pixel removed"

    print reduced_color_image.shape
    print reduced_color_image.dtype

    return reduced_color_image

# outputSeamCarvingRemoveObjectBeachWithPerson = removed_marked_object('inputSeamCarvingBeachWithPerson.jpg', 25 ,0)
# plot.subplot(2,1,1)
# plot.imshow(imread('inputSeamCarvingBeachWithPerson.jpg'))
# plot.subplot(2,1,2)
# plot.imshow(outputSeamCarvingRemoveObjectBeachWithPerson)
# imsave('outputSeamCarvingBeachWithPersonRemoved.png',outputSeamCarvingRemoveObjectBeachWithPerson)
# plot.show()