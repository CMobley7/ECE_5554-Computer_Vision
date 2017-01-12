# from scipy.misc import imread
# import matplotlib.pyplot as plot

def quantizeHSV(origImg, k):
    from skimage.color import rgb2hsv, hsv2rgb
    import numpy as np
    from scipy.cluster.vq import kmeans2

    input_HSV_image = rgb2hsv(origImg)
    reshaped_input_hue_channel = np.reshape(input_HSV_image[:,:,0],(-1,1))

    meanHues, labels = kmeans2(reshaped_input_hue_channel, k)

    reshaped_output_hue_channel = meanHues[labels]
    output_hue_channel = np.reshape(reshaped_output_hue_channel,(input_HSV_image[:,:,0].shape))

    output_HSV_image = input_HSV_image
    output_HSV_image[:,:,0] = output_hue_channel

    outputImg = (np.around(hsv2rgb(output_HSV_image) * 255)).astype(np.uint8)

    return outputImg, meanHues

# outputImg, meanHues = quantizeHSV(imread('fish.jpg'),3)
# print imread('fish.jpg').shape
# print imread('fish.jpg').dtype
# print outputImg.shape
# print outputImg.dtype
# print meanHues.shape
# print meanHues.dtype
# plot.subplot(1,2,1)
# plot.imshow(imread('fish.jpg'))
# plot.subplot(1,2,2)
# plot.imshow(outputImg)
# plot.show()