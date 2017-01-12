# from scipy.misc import imread
# from energy_image import energy_image
# import matplotlib.pyplot as plot

def mark_object(input_color_image, energyImage):
    import numpy as np
    import matplotlib.pyplot as plot
    from skimage.draw import polygon,set_color

    plot.imshow(input_color_image)

    print "Make a box around the object you would like to delete by click at each corner of the box you would like to make."
    selected_points = plot.ginput(4)

    x = np.array([selected_points[0][0],selected_points[1][0],selected_points[2][0],selected_points[3][0]])
    y = np.array([selected_points[0][1],selected_points[1][1],selected_points[2][1],selected_points[3][1]])
    rr,cc = polygon(y,x)
    energyImage = energyImage + 1000
    set_color(energyImage,(rr,cc), 0)
    return energyImage

# energyImage = mark_object(imread('inputSeamCarvingPrague.jpg'),energy_image(imread('inputSeamCarvingPrague.jpg')))
# plot.imshow(energyImage)
# plot.show()