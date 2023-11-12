from sklearn.datasets import make_regression, make_classification, make_blobs


# a dataset intended for use with linear regression, then the make_regression method
def regression():
    # Generate feature matrix, target vector and true coefficients
    features, target, coefficients = make_regression(n_samples=100,
                                                     n_features=3,
                                                     n_informative=3,
                                                     # retargets=1,
                                                     noise=0.0,
                                                     coef=True,
                                                     random_state=1)

    # Take a look at the matrix of features and the vector of goals
    print('Feature matrix    :', features[:3])
    print('Vector of targets:', target[:3])


# # of the dataset for the classification task, then you can use the make ciassification method
def classification():
    # Generate a feature matrix and a vector of goals
    features, target = make_classification(n_samples=100,
                                           n_features=3,
                                           n_informative=3,
                                           n_redundant=0,
                                           n_classes=2,
                                           weights=[.25, .75],
                                           random_state=1)

    print('Feature matrix    :', features[:3])
    print('Vector of targets:', target[:3])


# the dataset worked well with clustering methods,
# then the scikit-learn library offers a method for creating clusters of points
def clustering():
    features, target = make_blobs(n_samples=100,
                                  n_features=2,
                                  centers=3,
                                  cluster_std=0.5,
                                  shuffle=True,
                                  random_state=1)

    print('Feature matrix    :', features[:3])
    print('Vector of targets:', target[:3])


    import matplotlib.pyplot as plt
    plt.scatter(features[:, 0], features[:, 1], c=target)
    plt.show()


if __name__ == '__main__':
    # regression()
    # classification()
    clustering()
