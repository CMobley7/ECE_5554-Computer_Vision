from numpy.linalg import inv
import numpy as np
import matplotlib.pyplot as plot

def warpImage(inputIm, H, input_image_correspondences_points):

    input_image_correspondences_points = np.append(input_image_correspondences_points,np.ones((1, input_image_correspondences_points.shape[1])),axis=0)
    normalized_front_view_boundaries = np.dot(H, input_image_correspondences_points)

    front_view_boundaries = np.zeros((normalized_front_view_boundaries.shape[0]-1,normalized_front_view_boundaries.shape[1]))
    front_view_boundaries[0,:] = np.around(normalized_front_view_boundaries[0,:]/normalized_front_view_boundaries[2,:])
    front_view_boundaries[1,:] = np.around(normalized_front_view_boundaries[1,:]/normalized_front_view_boundaries[2,:])

    min_column_front_view, max_column_front_view = np.amin(front_view_boundaries[0,:]), np.amax(front_view_boundaries[0,:])
    min_row_front_view, max_row_front_view = np.amin(front_view_boundaries[1,:]), np.amax(front_view_boundaries[1,:])

    x_front_view = np.arange(min_column_front_view, max_column_front_view, 1)
    y_front_view = np.arange(min_row_front_view, max_row_front_view, 1)

    xv_front_view, yv_front_view = np.meshgrid(x_front_view, y_front_view, sparse=False, indexing='xy')

    meshgrid_front_view = np.array([np.ravel(xv_front_view),np.ravel(yv_front_view),np.ravel(np.ones(xv_front_view.shape))])

    invH = inv(H)

    normalized_correspondences_front_view = np.dot(invH, meshgrid_front_view)

    correspondences_front_view = np.zeros((normalized_correspondences_front_view.shape[0]-1, normalized_correspondences_front_view.shape[1]))
    correspondences_front_view[0,:] = np.around(normalized_correspondences_front_view[0,:]/normalized_correspondences_front_view[2,:])
    correspondences_front_view[1,:] = np.around(normalized_correspondences_front_view[1,:]/normalized_correspondences_front_view[2,:])
    correspondences_front_view = np.reshape(np.transpose(correspondences_front_view),(xv_front_view.shape[0],xv_front_view.shape[1],2))

    front_view_image = np.zeros((xv_front_view.shape[0],xv_front_view.shape[1],3))

    for ith_row in xrange(0, front_view_image.shape[0]):
        for ith_column in xrange(0, front_view_image.shape[1]):
            if correspondences_front_view[ith_row, ith_column, 0] < 0 or correspondences_front_view[ith_row, ith_column, 0] > inputIm.shape[1] - 1\
                    or correspondences_front_view[ith_row, ith_column, 1] < 0 or correspondences_front_view[ith_row, ith_column, 1] > inputIm.shape[0] - 1:
                front_view_image[ith_row, ith_column] = np.array([0,0,0])
            else:
                front_view_image[ith_row,ith_column] = np.array(inputIm[correspondences_front_view[ith_row,ith_column,1],correspondences_front_view[ith_row,ith_column,0],:])

    front_view_image = np.asarray(front_view_image, dtype=np.uint8)

    return front_view_image

if __name__ == "__main__":
    from scipy.misc import imread,imsave
    from computeH_extracredit import computeH
    front_view_image = warpImage(imread('tile1.jpg'),computeH(np.load('tile1_points.npy')), np.load("tile1_points.npy"))
    plot.subplot(1,1,1)
    plot.imshow(front_view_image)
    imsave("tile1_front_view.png", front_view_image)
    plot.show()
