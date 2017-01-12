# from scipy.misc import imread
# import matplotlib.pyplot as plot

def quantizeRGB(origImg, k):
    import numpy as np
    from scipy.cluster.vq import kmeans2

    input_image = origImg.astype(np.float64)
    reshaped_input_image = np.reshape(input_image, (-1, 3))

    meanColors, labels = kmeans2(reshaped_input_image, k)

    reshaped_output_image = meanColors[labels,:]
    outputImg = np.reshape(reshaped_output_image,(input_image.shape)).astype(np.uint8)

    return outputImg, meanColors


# outputImg, meanColors = quantizeRGB(imread('fish.jpg'),3)
# plot.subplot(1,2,1)
# plot.imshow(imread('fish.jpg'))
# plot.subplot(1,2,2)
# plot.imshow(outputImg)
# plot.show()