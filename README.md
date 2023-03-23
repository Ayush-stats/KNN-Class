# KNN-Class

Calculate distances: Calculate the distances between the test data and each point in the training set. The distance can be calculated using the Euclidean distance formula, which is the square root of the sum of the squared differences between the corresponding features of the two data points.

Find the k-nearest neighbors: Sort the distances in ascending order and select the k-nearest neighbors based on the calculated distance values.

Classify the test data: After selecting the k-nearest neighbors, determine the class label of the test data based on the majority class of its neighbors. If the majority of the neighbors belong to a certain class, the test data will be classified as belonging to that class.

Evaluate the algorithm: Finally, evaluate the accuracy of the KNN algorithm by comparing the predicted class labels with the actual class labels of the test data.
