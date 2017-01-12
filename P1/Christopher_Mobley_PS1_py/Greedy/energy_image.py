# import matplotlib.pyplot as plot
# from scipy.misc import imread, imsave


def energy_image(im):
    import numpy as np
    from scipy.ndimage.filters import convolve
    import skimage
    from skimage import color

    input_color_image = skimage.img_as_float(color.rgb2gray(im))
    gradient_x = convolve(input_color_image, np.array([[1,-1]]), mode="wrap")
    # gradient_x_with_roberts = convolve(input_color_image, np.array([[0, 1], [-1, 0]]), mode="wrap")
    gradient_y = convolve(input_color_image, np.array([[1],[-1]]),mode="wrap")
    # gradient_y_with_roberts = convolve(input_color_image, np.array([[1, 0], [0, -1]]), mode="wrap")
    energyImage = np.sqrt((gradient_x**2)+ (gradient_y**2))
    # energyImageWithRoberts = np.sqrt((gradient_x_with_roberts**2)+(gradient_y_with_roberts**2))
    return energyImage
    # return energyImageWithRoberts

# energyImage = energy_image(imread('inputSeamCarvingPrague.jpg'))
# imsave('outputEnergyImagePrague.png', energyImage)
# plot.imshow(energyImage)

# energyImageWithRoberts = energy_image(imread('inputSeamCarvingPrague.jpg'))
# imsave('outputEnergyImagePragueWithRoberts.png', energyImageWithRoberts)
# plot.imshow(energyImageWithRoberts)

# plot.show()