
def imgradient(input_image):
    import numpy as np
    from scipy.ndimage.filters import convolve
    import skimage
    from skimage import color

    input_color_image = skimage.img_as_float(color.rgb2gray(input_image))

    gradient_x = convolve(input_color_image, np.array([[1,-1]]), mode="wrap")
    gradient_y = convolve(input_color_image, np.array([[1],[-1]]),mode="wrap")
    gradient_x[gradient_x == 0] = .0000000001
    gradient_magnitude = np.sqrt(np.power(gradient_x,2)+ np.power(gradient_y,2))
    gradient_direction = np.arctan(gradient_y/gradient_x)

    return gradient_magnitude,gradient_direction

