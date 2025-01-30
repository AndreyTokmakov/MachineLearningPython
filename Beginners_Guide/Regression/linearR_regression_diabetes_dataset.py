
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, model_selection

def load_dataset():
    X, y = datasets.load_diabetes(return_X_y=True)
    print(X.shape)
    print(X[0])

    print('----------------------- Selecting the 3rd feature')
    X = X[:, 2]
    print(X.shape)

    print('---------------------- Reshaping to get a 2D array')
    X = X.reshape(-1, 1)
    print(X.shape)
    print(X)




if __name__ == '__main__':
    # load_dataset()



    X, y = datasets.load_diabetes(return_X_y=True)
    X = X[:, 2]
    X = X.reshape(-1, 1)

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.33)

    model = linear_model.LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    plt.scatter(X_test, y_test, color='black')
    plt.plot(X_test, y_pred, color='blue', linewidth=3)
    plt.xlabel('Scaled BMIs')
    plt.ylabel('Disease Progression')
    plt.title('A Graph Plot Showing Diabetes Progression Against BMI')
    plt.show()