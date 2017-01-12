import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread, imresize, imsave

#Original Image
img = imread('inputPS0Q2.jpg')

img_red = img[...,0]
img_green = img[...,1]
img_blue = img[...,2]

#Load the input color image and swap its red and green color channels.
#Save the output as swapImgPS0Q2.png
img_swap = np.zeros(img.shape,dtype=np.uint8)
img_swap[...,0] = img_green
img_swap[...,1] = img_red
img_swap[...,2] = img_blue
imsave("swapImgPS0Q2.png",img_swap)
plt.subplot(3,2,1)
plt.imshow(img_swap)
plt.title('Original Image with R and G Channel Swapped')

#Convert the input color image to a grayscale image. Save the output
#as grayImgPS0Q2.png

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

img_gray = np.uint8(rgb2gray(img))
imsave("grayImgPS0Q2.png",img_gray)
plt.subplot(3,2,2)
plt.imshow(img_gray, cmap = plt.get_cmap("gray"))
plt.title("Original Image to Gray Scale")

#Convert the grayscale image to its negative image, in which the
#lightest values appear dark and vice versa. Save the output as
#negativeImgPS0Q2.png

img_negative = np.invert(img_gray)
imsave("negativeImgPS0Q2.png",img_negative)
plt.subplot(3,2,3)
plt.imshow(img_negative, cmap = plt.get_cmap("gray"))
plt.title("Invert Gray Scale Image")

#Map the grayscale image to its mirror image, i.e., flipping it
#left to right. Save the output as mirrorImgPS0Q2.png.
img_flipl2r = np.fliplr(img_gray)
imsave("mirrorImgPS0Q2.png", img_flipl2r)
plt.subplot(3,2,4)
plt.imshow(img_flipl2r, cmap = plt.get_cmap("gray"))
plt.title("Gray Scale Image Flipped Left to Right")

#Average the grayscale image with its mirror image (use typecasting).
#Save the output as avgImgPS0Q2.png.

img_average = np.uint8((img_gray + img_flipl2r)/2)
imsave("avgImgPS0Q2.png", img_average)
plt.subplot(3,2,5)
plt.imshow(img_average, cmap = plt.get_cmap("gray"))
plt.title("Gray Scaled and Imaged Flipped Left to Right Averaged")

#Create a matrix N whose size is same as the grayscale image, containing
#random numbers in the range [0 255]. Save this matrix in a file called
#noise.mat(npy). Add N to the grayscale image, then clip the resulting
#image to have a maximum value of 255. Save the output as addNoiseImgPS0Q2.png.

N = np.random.random_integers(0, high=255, size=img_gray.shape)
np.save("noise.npy", N)
img_add_noise = np.uint8(img_gray + N)
imsave("addNoiseImgPS0Q2.png",img_add_noise)
plt.subplot(3,2,6)
plt.imshow(img_add_noise,cmap = plt.get_cmap("gray"))
plt.title("Gray Scale Image with Noise Added")
plt.show()


