import matplotlib.pyplot as plot
from scipy.misc import imsave

def SeamCarvingReduceHeight(im,desired_reduction):
    from scipy.misc import imread
    from energy_image import energy_image
    from reduceHeight import reduceHeight

    input_color_image = imread(im)
    print input_color_image.shape
    print input_color_image.dtype
    input_energy_image = energy_image(input_color_image)
    reduced_color_image = input_color_image
    reduced_energy_image = input_energy_image

    for ith_pixel in xrange(0, desired_reduction):
        reduced_color_image,reduced_energy_image = reduceHeight(reduced_color_image,reduced_energy_image)
        print str(ith_pixel+1) + " pixel removed"

    return reduced_color_image

outputReduceHeightPrague = SeamCarvingReduceHeight('inputSeamCarvingPrague.jpg', 100)
imsave('outputReduceHeightPrague.png', outputReduceHeightPrague)
plot.subplot(1,2,1)
plot.imshow(outputReduceHeightPrague)

outputReduceHeightMall = SeamCarvingReduceHeight('inputSeamCarvingMall.jpg', 100)
imsave('outputReduceHeightMall.png', outputReduceHeightMall)
plot.subplot(1,2,2)
plot.imshow(outputReduceHeightMall)

plot.show()