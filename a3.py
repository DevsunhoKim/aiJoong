import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Define input and target data
x = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])
train_input, test_input, train_target, test_target = train_test_split(x, y, test_size=0.2, random_state=42)

x0 = np.ones((train_input.shape[0], 1))
X = np.hstack((x0, train_input))
print(X.shape)
w = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(train_target)
print(w)
plt.scatter(train_input, train_target)
plt.plot([0, 50], [w[0], 50*w[1]+w[0]], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

lr = LinearRegression()
lr.fit(train_input, train_target)
score = lr.score(test_input, test_target)
y_pred = lr.predict(test_input)
r2 = 1 - ((test_target - y_pred)**2).sum() / ((test_target - test_target.mean())**2).sum()
print(score)
print(lr.coef_, lr.intercept_)
plt.scatter(train_input, train_target)
plt.plot([0, 50], [lr.intercept_, 50 * lr.coef_ + lr.intercept_], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

lr_no_intercept = LinearRegression(fit_intercept=False)
lr_no_intercept.fit(train_input, train_target)
print(lr_no_intercept.coef_, lr_no_intercept.intercept_)
plt.scatter(train_input, train_target)
plt.plot([0, 50],
         [lr_no_intercept.intercept_, 50 * lr_no_intercept.coef_ +
          lr_no_intercept.intercept_], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
