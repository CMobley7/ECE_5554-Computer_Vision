import numpy as np

def predictAction(testMoments, trainMoments, trainLabels):

    #initilize variables
    distances = np.zeros((1, trainMoments.shape[0]))

    #reshape testMoments to be a 7x1 array
    testMoments = np.reshape(testMoments,(-1,1))

    #calculate variance
    variance = np.reshape(np.nanvar(trainMoments,axis=0),(-1,1))

    #calculate normalized Euclidean distance between testMoment and each trainMoment
    for ith_train_moment in xrange(0, trainMoments.shape[0]):
        distances[:,ith_train_moment] = np.sqrt(np.sum(np.divide(np.power(np.reshape(trainMoments[ith_train_moment,:],(-1,1))-testMoments,2),variance)))

    #sort distances
    sorted_index = np.argsort(distances)

    #sort labels and set predictedAction to the first label
    predictedAction = int(trainLabels[sorted_index][0,0])

    return predictedAction

if __name__ == "__main__":
    testMoments = np.load('botharms-up-p1-1_huVector.npy')
    # testMoments = np.load('crouch-p1-1_huVector.npy')
    # testMoments = np.load('rightkick-p1-1_huVector.npy')
    trainMoments = np.asarray(np.load('huVectors.npy'))
    trainLabels = np.array([[1],[1],[1],[1],[2],[2],[2],[2],[3],[3],[3],[3],[4],[4],[4],[4],[5],[5],[5],[5]])
    predictedAction = predictAction(testMoments,trainMoments,trainLabels)
    print predictedAction