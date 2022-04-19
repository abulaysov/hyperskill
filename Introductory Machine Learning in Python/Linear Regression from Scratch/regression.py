import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


class CustomLinearRegression:

    def __init__(self, *, fit_intercept=True):

        self.fit_intercept = fit_intercept
        self.coefficient = None
        self.intercept = None

    def fit(self, X, y):
        if self.fit_intercept:
            X = np.column_stack((np.ones_like(y), X))
            b = np.linalg.solve(X.T @ X, X.T @ y)
            self.intercept, self.coefficient = b[0], b[1:]
        else:
            self.coefficient = np.linalg.solve(X.T @ X, X.T @ y)

    def predict(self, X):
        yhat = X @ self.coefficient
        if self.fit_intercept:
            yhat += np.ones_like(yhat) * self.intercept

        return yhat

    @staticmethod
    def r2_score(y, yhat):
        return 1 - np.sum((y - yhat) ** 2) / np.sum((y - np.mean(y)) ** 2)

    @staticmethod
    def rmse(y, yhat):
        return np.sqrt(np.mean((y - yhat) ** 2))


def print_diff(mod1, mod2, X, y):
    yhat1, yhat2 = mod1.predict(X), mod2.predict(X)
    rmse1, rmse2 = mean_squared_error(y, yhat1) ** 0.5, mean_squared_error(y, yhat2) ** 0.5
    r21, r22 = r2_score(y, yhat1), r2_score(y, yhat2)
    print({'Intercept': np.abs(mod1.intercept - mod2.intercept_),
           'Coefficient': np.abs(mod1.coefficient - mod2.coef_),
           'R2': np.abs(r21 - r22),
           'RMSE': np.abs(rmse1 - rmse2)})


def main():
    s = """
    f1  f2  f3  y
    2.31    65.2    15.3    24.0
    7.07    78.9    17.8    21.6
    7.07    61.1    17.8    34.7
    2.18    45.8    18.7    33.4
    2.18    54.2    18.7    36.2
    2.18    58.7    18.7    28.7
    7.87    96.1    15.2    27.1
    7.87    100.0   15.2    16.5
    7.87    85.9    15.2    18.9
    7.87    94.3    15.2    15.0"""
    lines = s.split('\n')[1:-1]
    col_names = lines[0].split()
    data = []
    for line in lines[1:]:
        data.append([float(x) for x in line.split()])
    df = pd.DataFrame(np.array(data))
    df.columns = col_names
    X, y = df[['f1', 'f2', 'f3']].values, df['y'].values
    lr = CustomLinearRegression()
    regSci = LinearRegression(fit_intercept=True)
    lr.fit(X, y)
    regSci.fit(X, y)
    print_diff(lr, regSci, X, y)


if __name__ == '__main__':
    main()
