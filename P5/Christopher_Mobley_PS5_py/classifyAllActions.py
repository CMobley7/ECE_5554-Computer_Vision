import numpy as np

def classifyAllActions(testMoments, trainMoments, trainLabels, K):

#initilize variables
    distances = np.zeros((1, trainMoments.shape[0]))
    nearestLabel = np.zeros((480, 640, K))

    #reshape testMoments to be a 7x1 array
    testMoments = np.reshape(testMoments,(-1,1))

    #calculate variance
    variance = np.reshape(np.nanvar(trainMoments,axis=0),(-1,1))

    #calculate normalized Euclidean distance between testMoment and each trainMoment
    for ith_train_moment in xrange(0, trainMoments.shape[0]):
        distances[:,ith_train_moment] = np.sqrt(np.sum(np.divide(np.power(np.reshape(trainMoments[ith_train_moment,:],(-1,1))-testMoments,2),variance)))

    #return indicies of sorted distances
    sorted_index = np.argsort(distances)

    #sort trainLabels by indicies
    sorted_predicted_actions = trainLabels[sorted_index].flatten()

    #determine and return the most frequent neighbor with k = K
    k_predicted_actions = sorted_predicted_actions[0:K]
    count = np.bincount(k_predicted_actions)
    predictedAction = np.argmax(count)

    return predictedAction

if __name__ == "__main__":
    #initilize variables
    trainMoments = np.asarray(np.load('huVectors.npy'))
    trainLabels = np.array([[1],[1],[1],[1],[2],[2],[2],[2],[3],[3],[3],[3],[4],[4],[4],[4],[5],[5],[5],[5]])
    K = 4
    predicted_actions = np.zeros((trainLabels.shape), dtype=np.float64)
    confusion_matrix = np.zeros((5,5), dtype=np.float64)
    mean_recognition_rate = np.zeros((5,1))
    train_nth_row, train_nth_column = trainMoments.shape
    cm_nth_row,cm_nth_column = confusion_matrix.shape

    #classify all actions with their most frequent neighbor with k = K
    for ith_Moment in xrange(0,train_nth_row):
        test_moments = trainMoments[ith_Moment,:]
        train_labels = np.delete(trainLabels,ith_Moment,0)
        train_moments = np.delete(trainMoments,ith_Moment,0)
        predicted_actions[ith_Moment,:] = classifyAllActions(test_moments, train_moments, train_labels, K)

    #compute confusion matrix
    for ith_action in xrange(0,train_nth_row):
        confusion_matrix[trainLabels[ith_action,:][0]-1,predicted_actions[ith_action,:][0]-1] = confusion_matrix[trainLabels[ith_action,:][0]-1,predicted_actions[ith_action,:][0]-1] + 1
    np.save("confusion_matrix.npy", confusion_matrix)

    #compute mean recognition rate
    for ith_row in xrange(0,cm_nth_column):
        mean_recognition_rate[ith_row,:] = np.float(confusion_matrix[ith_row,ith_row] / 4)
    np.save("mean_recognition_rate.npy", mean_recognition_rate)

    #report mean recognition rate and confusion matrix
    print mean_recognition_rate
    print confusion_matrix





