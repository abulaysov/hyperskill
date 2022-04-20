import math

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression


class CustomLogisticRegression:

    def __init__(self, fit_intercept=True, l_rate=0.01, n_epoch=100):
        self.fit_intercept = fit_intercept
        self.l_rate = l_rate
        self.n_epoch = n_epoch
        self.coef_ = np.array([])
        self.mse_error_first = []
        self.mse_error_last = []
        self.log_loss_error_first = []
        self.log_loss_error_last = []

    def sigmoid(self, t):
        return 1 / (1 + math.e ** -t)

    def predict_proba(self, row, coef_):
        if self.fit_intercept:
            t = row @ coef_[1:] + coef_[0]
            return self.sigmoid(t)
        else:
            return self.sigmoid(row @ coef_)

    def fit_mse(self, X_train, y_train):
        r, c = X_train.shape
        self.coef_ = np.zeros(c + 1 if self.fit_intercept else c)
        for n in range(self.n_epoch):
            for i, row in enumerate(X_train):
                y_hat = self.predict_proba(row, self.coef_)
                if n == 0:
                    self.mse_error_first.append((y_hat - y_train[i]) ** 2 / r)
                elif n == self.n_epoch - 1:
                    self.mse_error_last.append((y_hat - y_train[i]) ** 2 / r)
                if self.fit_intercept:
                    self.coef_[0] = self.coef_[0] - self.l_rate * (y_hat - y_train[i]) * y_hat * (1 - y_hat)
                    for j in range(row.size):
                        self.coef_[j + 1] = self.coef_[j + 1] - self.l_rate * (y_hat - y_train[i]) * y_hat * (
                                    1 - y_hat) * row[j]
                else:
                    for j in range(row.size):
                        self.coef_[j] = self.coef_[j] - self.l_rate * (y_hat - y_train[i]) * y_hat * (1 - y_hat) * row[
                            j]

    def fit_log_loss(self, X_train, y_train):
        r, c = X_train.shape
        self.coef_ = np.zeros(c + 1 if self.fit_intercept else c)
        for n in range(self.n_epoch):
            for i, row in enumerate(X_train):
                y_hat = self.predict_proba(row, self.coef_)
                if n == 0:
                    self.log_loss_error_first.append(
                        (y_train[i] * math.log(y_hat) + (1 - y_train[i]) * math.log(1 - y_hat)) / -r)
                elif n == self.n_epoch - 1:
                    self.log_loss_error_last.append(
                        (y_train[i] * math.log(y_hat) + (1 - y_train[i]) * math.log(1 - y_hat)) / -r)
                if self.fit_intercept:
                    self.coef_[0] = self.coef_[0] - self.l_rate * (y_hat - y_train[i]) / r
                    for j in range(row.size):
                        self.coef_[j + 1] = self.coef_[j + 1] - self.l_rate * (y_hat - y_train[i]) * row[j] / r
                else:
                    for j in range(row.size):
                        self.coef_[j] = self.coef_[j] - self.l_rate * (y_hat - y_train[i]) * row[j] / r

    def predict(self, X_test, cut_off=0.5):
        predictions = []
        for row in X_test:
            y_hat = self.predict_proba(row, self.coef_)
            if y_hat < cut_off:
                predictions.append(0)
            else:
                predictions.append(1)
        return predictions


X, y = load_breast_cancer(return_X_y=True, as_frame=True)
X = X[['worst concave points', 'worst perimeter', 'worst radius']].to_numpy()
y = y.to_numpy()
scaler = StandardScaler()
X = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=43)

model_mse = CustomLogisticRegression(n_epoch=1000)
model_log = CustomLogisticRegression(n_epoch=1000)
model = LogisticRegression()

model_mse.fit_mse(X_train, y_train)
y_pred_mse = model_mse.predict(X_test)
accuracy_mse = accuracy_score(y_test, y_pred_mse)

model_log.fit_log_loss(X_train, y_train)
y_pred_log = model_log.predict(X_test)
accuracy_log = accuracy_score(y_test, y_pred_log)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

result = {'mse_accuracy': accuracy_mse,
          'logloss_accuracy': accuracy_log,
          'sklearn_accuracy': accuracy,
          'mse_error_first': model_mse.mse_error_first,
          'mse_error_last': model_mse.mse_error_last,
          'logloss_error_first': model_log.log_loss_error_first,
          'logloss_error_last': model_log.log_loss_error_last}
mse_min_first = round(min(model_mse.mse_error_first), 5)
mse_min_last = round(min(model_mse.mse_error_last), 5)
log_max_first = round(max(model_log.log_loss_error_first), 5)
log_max_last = round(max(model_log.log_loss_error_last), 5)

print(result)
print(
    f'Answers to the questions:\n1) {mse_min_first:.5f}\n2) {mse_min_last:.5f}\n3) {log_max_first:.5f}\n4) {log_max_last:.5f}\n5) expanded\n6) expanded')
