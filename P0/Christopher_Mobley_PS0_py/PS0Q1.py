import numpy as np
import matplotlib.pyplot as plt

A = np.load("inputAPS0Q1.npy")

#a
#Plot all the intensities in A, sorted in decreasing value.
#Provide the plot in your answer sheet. (Note, in this case
#we don’t care about the 2D structure of A, we only want to
#sort the list of all intensities.)
x = np.arange(10000)
y = (np.sort(A, axis = None))[::-1]
plt.plot(x, y)
plt.show()

#b
#Display a histogram of A’s intensities with 20 bins. Again,
#we do not care about the 2D structure. Provide the histogram
#in your answer sheet.

plt.hist(A,bins=20)
plt.show()

#c
#Create a new matrix X that consists of the bottom left quadrant
#of A. Display X as an image in your answer sheet using
#matplotlib.pyplot.imshow with no interpolation (blurry effect).
#Look at the documentation for matplotlib.pyplot.imshow. Save X
#in a file called outputXPS0Q1.npy and submit the file.

X = A[:50,50:]
np.save("outputXPS0Q1.npy", X)
plt.imshow(X, interpolation = None)
plt.show()


#d
#Create a new matrix Y, which is the same as A, but with A’s mean
#intensity value subtracted from each pixel. Display Y as an image
#in your answer sheet using matplotlib.pyplot.imshow. Save Y in a
#file called outputYPS0Q1.npy and submit the file.

mean = np.average(A)
Y = A - mean
np.save("outputYPS0Q1.npy", Y)
plt.imshow(Y, interpolation = None)
plt.show()

#e
#Create a new matrix Z that represents a color image the same size
#as A, but with 3 channels to represent R, G and B values. Set the
#values to be red (i.e., R = 1, G = 0, B = 0) wherever the intensity
#in A is greater than a threshold t = the average intensity in A, and
#black everywhere else. Display Z as an image in your answer sheet
#using matplotlib.pyplot.imshow. Save Z as outputZPS0Q1.png and submit
#the file. Be sure to view outputZPS0Q1.png in an image viewer to make
#sure it looks right.

#e
#Create a new matrix Z that represents a color image the same size
#as A, but with 3 channels to represent R, G and B values. Set the
#values to be red (i.e., R = 1, G = 0, B = 0) wherever the intensity
#in A is greater than a threshold t = the average intensity in A, and
#black everywhere else. Display Z as an image in your answer sheet
#using matplotlib.pyplot.imshow. Save Z as outputZPS0Q1.png and submit
#the file. Be sure to view outputZPS0Q1.png in an image viewer to make
#sure it looks right.

Z = np.zeros((100,100,3),'float64')
Z[A > mean] = [1, 0, 0]
np.save('outputZPS0Q1.png', Z)
plt.imshow(Z, interpolation = None)
plt.show()



