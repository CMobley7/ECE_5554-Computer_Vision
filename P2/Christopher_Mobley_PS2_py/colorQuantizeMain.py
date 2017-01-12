from scipy.misc import imread

def colorQuantizeMain(input_image,k):
    from quantizeRGB import quantizeRGB
    from quantizeHSV import quantizeHSV
    from computeQuantizationError import computeQuantizationError
    from getHueHists import getHueHists
    import matplotlib.pyplot as plot
    from scipy.misc import imsave

    output_quantizeRGB_image, mean_colors = quantizeRGB(input_image,k)

    imsave("output_quantizeRGB_image_k_"+str(k)+".png",output_quantizeRGB_image)
    plot.subplot(2,2,1)
    plot.imshow(output_quantizeRGB_image)
    plot.title("Quantize RGB with k=" + str(k))

    error_RGB = computeQuantizationError(input_image,output_quantizeRGB_image)

    output_quantizeHSV_image, mean_hues = quantizeHSV(input_image,k)
    imsave("output_quantizeHSV_image_k_"+str(k)+".png",output_quantizeHSV_image)
    plot.subplot(2,2,2)
    plot.imshow(output_quantizeHSV_image)
    plot.title("Quantize HSV with k=" + str(k))

    error_HSV = computeQuantizationError(input_image,output_quantizeHSV_image)
    hist_equal, hist_clustered = getHueHists(input_image,k)
    plot.subplot(2,2,3)
    plot.title("Equally Spaced Bins with k=" + str(k))
    plot.subplot(2,2,4)
    plot.title("K Cluster Center Membership Bins with k=" + str(k))
    plot.show()

    return error_RGB,error_HSV,hist_equal,hist_clustered

error_RGB_2,error_HSV_2,hist_equal_2,hist_clustered_2 = colorQuantizeMain(imread('fish.jpg'), 2)
print "for k = 2"
print "error_RGB = " + str(error_RGB_2)
print "error_HSV = " + str(error_HSV_2)
print "bin count for equally spaced bins is" + str(hist_equal_2)
print "bin count for bins defined by the k cluster center membership" + str(hist_clustered_2)

error_RGB_4,error_HSV_4,hist_equal_4,hist_clustered_4 = colorQuantizeMain(imread('fish.jpg'), 4)
print "for k = 4"
print "error_RGB = " + str(error_RGB_4)
print "error_HSV = " + str(error_HSV_4)
print "bin count for equally spaced bins is" + str(hist_equal_4)
print "bin count for bins defined by the k cluster center membership" + str(hist_clustered_4)

error_RGB_6,error_HSV_6,hist_equal_6,hist_clustered_6 = colorQuantizeMain(imread('fish.jpg'), 6)
print "for k = 6"
print "error_RGB = " + str(error_RGB_6)
print "error_HSV = " + str(error_HSV_6)
print "bin count for equally spaced bins is" + str(hist_equal_6)
print "bin count for bins defined by the k cluster center membership" + str(hist_clustered_6)

