import matplotlib.pyplot as plot
from scipy.misc import imsave,imshow,imread

def  SeamCarvingReduceWidth(im,desired_reduction):
    from scipy.misc import imread
    from energy_image import energy_image
    from reduceWidth import reduceWidth

    input_color_image = imread(im)
    print input_color_image.shape
    print input_color_image.dtype
    input_energy_image = energy_image(input_color_image)
    reduced_color_image = input_color_image
    reduced_energy_image = input_energy_image

    for ith_pixel in xrange(0, desired_reduction):
        reduced_color_image,reduced_energy_image = reduceWidth(reduced_color_image,reduced_energy_image)
        print str(ith_pixel+1) + " pixel removed"

    return reduced_color_image

outputReduceWidthPrague = SeamCarvingReduceWidth('inputSeamCarvingPrague.jpg', 100)
imsave('outputReduceWidthPrague.png', outputReduceWidthPrague)
plot.subplot(1,2,1)
plot.imshow(outputReduceWidthPrague)

outputReduceWidthMall = SeamCarvingReduceWidth('inputSeamCarvingMall.jpg', 100)
imsave('outputReduceWidthMall.png', outputReduceWidthMall)
plot.subplot(1,2,2)
plot.imshow(outputReduceWidthMall)

plot.show()