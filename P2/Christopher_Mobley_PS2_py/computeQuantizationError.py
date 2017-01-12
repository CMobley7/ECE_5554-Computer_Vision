# from scipy.misc import imread
# from quantizeRGB import quantizeRGB
# from quantizeHSV import quantizeHSV

def computeQuantizationError(origImg,quantizedImg):
    import numpy as np

    error = np.sum(np.power((origImg - quantizedImg),2))/(origImg.shape[0]*origImg.shape[1]*origImg.shape[2])

    return error

# print computeQuantizationError(imread('fish.jpg'),imread('fish.jpg'))
# print computeQuantizationError(imread('fish.jpg'),quantizeRGB(imread('fish.jpg'),3)[0])
# print computeQuantizationError(imread('fish.jpg'),quantizeHSV(imread('fish.jpg'),3)[0])