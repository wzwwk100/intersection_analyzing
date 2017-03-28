from sklearn.linear_model import LinearRegression
X = [[0.446, 0.59], [0.679, 0.664], [0.744, 0.718], [0.838, 0.666], [0.692, 0.731]]
y = [[5], [7], [8], [8], [8]]
model = LinearRegression()
model.fit(X, y)
X_test = [[0.672, 0.673], [0.952, 0.726], [0.539, 0.714], [0.716, 0.678]]
y_test = [[7], [10], [6], [7]]
predictions = model.predict(X_test)
for i, prediction in enumerate(predictions):
    print('Predicted: %s, Target: %s' % (prediction, y_test[i]))
print('R-squared: %.2f' % model.score(X_test, y_test))
