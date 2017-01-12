# from scipy.misc import imread
# import matplotlib.pyplot as plot

def getHueHists(im, k):
    from skimage.color import rgb2hsv
    import numpy as np
    from quantizeHSV import quantizeHSV
    import matplotlib.pyplot as plot

    reshaped_im_hue_channel = np.reshape(rgb2hsv(im)[:,:,0], (-1,1))

    plot.subplot(2,2,3)
    histEqual,equal_bin_edges ,_ = plot.hist(reshaped_im_hue_channel,bins=k)

    outputImg, meanHues = quantizeHSV(im,k)

    reshaped_outputImg_hue_channel = np.reshape(rgb2hsv(outputImg)[:,:,0],(-1,1))

    edges = np.zeros(((k+1),1))
    edges[1:-1] = ((np.sort(meanHues, axis=0)[:-1] + np.sort(meanHues, axis=0)[1:])/2)
    edges[0], edges[-1] = max(np.sort(meanHues, axis=0)[0] - edges[1],0), min(np.sort(meanHues, axis=0)[-1] + edges[-2],1)
    edges = edges[:,0]

    plot.subplot(2,2,4)
    histClustered, clustered_bin_edges, _ = plot.hist(reshaped_outputImg_hue_channel,bins=edges)

    return histEqual, histClustered

# histEqual, histClustered = getHueHists(imread('fish.jpg'),3)
# print "bin count for equally spaced bins is" + str(histEqual)
# print "bin count for bins defined by the k cluster center membership" + str(histClustered)
# plot.show()