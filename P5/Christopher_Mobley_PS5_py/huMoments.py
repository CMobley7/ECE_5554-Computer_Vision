import numpy as np

def u(p,q,H,X,Y,x_bar,y_bar):

    #calculate central moment
    central_moment = np.sum(np.power((X-x_bar),p) * np.power((Y-y_bar),q) * H, dtype=np.float64)

    return central_moment

def huMoments(H):
    #convert image to float data type
    np.asarray(H,dtype=np.float64)

    #calculate shape of image
    nth_row, nth_column = H.shape

    #create meshgrid
    x = np.arange(0, nth_column, 1)
    y = np.arange(0,nth_row,1)
    X,Y = np.meshgrid(x, y, sparse=False, indexing='xy')
    X += 1
    np.asarray(X,dtype=np.float64)
    Y += 1
    np.asarray(X,dtype=np.float64)

    #calcule raw image moments
    m_0_0 = np.sum(H, dtype=np.float64)
    m_1_0 = np.sum(X*H, dtype=np.float64)
    m_0_1 = np.sum(Y*H, dtype=np.float64)

    #calculate centroids
    x_bar = m_1_0/m_0_0
    y_bar = m_0_1/m_0_0

    #calculate applicable central moments for specified motion history image
    u_0_2 = u(0,2,H,X,Y,x_bar,y_bar)
    u_0_3 = u(0,3,H,X,Y,x_bar,y_bar)
    u_1_1 = u(1,1,H,X,Y,x_bar,y_bar)
    u_1_2 = u(1,2,H,X,Y,x_bar,y_bar)
    u_2_0 = u(2,0,H,X,Y,x_bar,y_bar)
    u_2_1 = u(2,1,H,X,Y,x_bar,y_bar)
    u_3_0 = u(3,0,H,X,Y,x_bar,y_bar)

    #calculate hu moments
    h_1 = u_2_0 + u_0_2
    h_2 = np.power((u_2_0 - u_0_2),2) + 4 * np.power(u_1_1,2)
    h_3 = np.power((u_3_0 - 3 * u_1_2),2) + np.power((3 * u_2_1 - u_0_3), 2)
    h_4 = np.power((u_3_0 + u_1_2),2) + np.power((u_2_1 + u_0_3), 2)
    h_5 = (u_3_0 - 3 * u_1_2) * (u_3_0 + u_1_2) * (np.power((u_3_0 + u_1_2),2) - 3 * np.power((u_2_1 + u_0_3), 2)) + (3 * u_2_1 - u_0_3) * (u_2_1 + u_0_3) * (3 * np.power((u_3_0 + u_1_2), 2) - np.power((u_2_1 + u_0_3), 2))
    h_6 = (u_2_0 - u_0_2) * (np.power((u_3_0 + u_1_2),2) - np.power((u_2_1 + u_0_3),2)) + 4 * u_1_1 * (u_3_0 + u_1_2) * (u_2_1 + u_0_3)
    h_7 = (3 * u_2_1 - u_0_3) * (u_3_0 + u_1_2) * (np.power((u_3_0 + u_1_2),2) - 3 * np.power((u_2_1 + u_0_3),2)) - (u_3_0 - 3 * u_1_2) * (u_2_1 + u_0_3) * (3 * np.power((u_3_0 + u_1_2), 2) - np.power((u_2_1 + u_0_3), 2))

    moments = [h_1, h_2, h_3, h_4, h_5, h_6, h_7]

    return moments

if __name__ == "__main__":

    #create three different hu vector for a testing of predictAction.py
    motion_history_image = np.load('botharms-up-p1-1_MHI.npy')
    huVector = huMoments(motion_history_image)
    np.save('botharms-up-p1-1_huVector.npy', huVector)

    motion_history_image = np.load('crouch-p1-1_MHI.npy')
    huVector = huMoments(motion_history_image)
    np.save('crouch-p1-1_huVector.npy', huVector)

    motion_history_image = np.load('rightkick-p1-1_MHI.npy')
    huVector = huMoments(motion_history_image)
    np.save('rightkick-p1-1_huVector.npy', huVector)

    #create hu vectore array of all MHIs
    #load data
    motion_history_images = np.load('allMHIs.npy')

    #initlize variables
    nth_row, nth_column, number_of_motition_history_images = motion_history_images.shape
    huVectors = np.zeros((number_of_motition_history_images,7))

    #calculate hu vector for each motion history image and store them as one hu vectors
    for ith_motion_history_image in xrange(0,number_of_motition_history_images):
        huVectors[ith_motion_history_image,:] = huMoments(motion_history_images[:,:,ith_motion_history_image])

    #save hu vectors
    np.save('huVectors.npy', huVectors)