from numpy.linalg import inv
import numpy as np
import matplotlib.pyplot as plot

def warpImage(inputIm, refIm, H):

    nth_row_input_image, nth_column_input_image, _ = inputIm.shape
    nth_row_reference_image, nth_column_reference_image, _ = refIm.shape

    input_image_boundaries = np.array([[0,nth_column_input_image-1,nth_column_input_image-1,0],[0,0,nth_row_input_image-1,nth_row_input_image-1],[1,1,1,1]])

    normalized_transformed_boundaries = np.dot(H,input_image_boundaries)

    transformed_boundaries = np.zeros((normalized_transformed_boundaries.shape[0]-1,normalized_transformed_boundaries.shape[1]))
    transformed_boundaries[0,:] = np.around(normalized_transformed_boundaries[0,:]/normalized_transformed_boundaries[2,:])
    transformed_boundaries[1,:] = np.around(normalized_transformed_boundaries[1,:]/normalized_transformed_boundaries[2,:])

    min_column_transformed_boundaries, max_column_transformed_boundaries = min(np.amin(transformed_boundaries[0,:]),0), np.amax(transformed_boundaries[0,:])
    min_row_transformed_boundaries, max_row_transformed_boundaries = min(np.amin(transformed_boundaries[1,:]),0), np.amax(transformed_boundaries[1,:])

    x = np.arange(min_column_transformed_boundaries, max_column_transformed_boundaries, 1)
    y = np.arange(min_row_transformed_boundaries, max_row_transformed_boundaries, 1)

    xv, yv = np.meshgrid(x, y, sparse=False, indexing='xy')

    meshgrid = np.array([np.ravel(xv),np.ravel(yv),np.ravel(np.ones(xv.shape))])

    invH = inv(H)

    normalized_correspondences = np.dot(invH, meshgrid)

    correspondences = np.zeros((normalized_correspondences.shape[0]-1, normalized_correspondences.shape[1]))
    correspondences[0,:] = np.around(normalized_correspondences[0,:]/normalized_correspondences[2,:])
    correspondences[1,:] = np.around(normalized_correspondences[1,:]/normalized_correspondences[2,:])
    correspondences = np.reshape(np.transpose(correspondences),(xv.shape[0],xv.shape[1],2))

    warpIm = np.zeros((xv.shape[0],xv.shape[1],3))

    for ith_row in xrange(0, warpIm.shape[0]):
        for ith_column in xrange(0, warpIm.shape[1]):
            if correspondences[ith_row, ith_column, 0] < 0 or correspondences[ith_row, ith_column, 0] > nth_column_input_image - 1\
                    or correspondences[ith_row, ith_column, 1] < 0 or correspondences[ith_row, ith_column, 1] > nth_row_input_image - 1:
                warpIm[ith_row, ith_column] = np.array([0,0,0])
            else:
                warpIm[ith_row,ith_column] = np.array(inputIm[correspondences[ith_row,ith_column,1],correspondences[ith_row,ith_column,0],:])

    warpIm = np.asarray(warpIm, dtype=np.uint8)

    mergeIm = np.copy(warpIm)
    mergeIm[abs(min_row_transformed_boundaries):abs(min_row_transformed_boundaries)+nth_row_reference_image,
    abs(min_column_transformed_boundaries):abs(min_column_transformed_boundaries)+nth_column_reference_image,:] = refIm

    return warpIm, mergeIm

if __name__ == "__main__":
    from scipy.misc import imread,imsave
    from computeH import computeH
    from getting_correspondences import getting_correspondences

    # warpIm, mergeIm = warpImage(imread('crop1.jpg'),imread('crop2.jpg'),computeH(np.transpose(np.load('cc1.npy')),np.transpose(np.load('cc2.npy'))))

    # t1, t2 = getting_correspondences(imread('wdc1.jpg'),imread('wdc2.jpg'))
    # np.save("points1.npy", t1)
    # np.save("points2.npy", t2)
    warpIm, mergeIm = warpImage(imread('wdc1.jpg'),imread('wdc2.jpg'),computeH(np.load('points1.npy'),np.load('points2.npy')))
    plot.subplot(1,2,1)
    plot.title("Warped Image")
    plot.imshow(warpIm)
    imsave("wdc1_warped.png", warpIm)
    plot.subplot(1,2,2)
    plot.title("Merged Image")
    plot.imshow(mergeIm)
    imsave("wdc_merged.png", mergeIm)
    plot.show()

