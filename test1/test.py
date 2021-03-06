from sklearn.linear_model import LinearRegression
X = [[0.446, 0.59], [0.679, 0.664], [0.744, 0.718], [0.838, 0.666], [0.692, 0.731], [0.672, 0.673], [0.952, 0.726], [0.539, 0.714], [0.716, 0.678], [0.766, 0.798], [0.849, 0.849], [0.584, 0.606], [0.72, 0.697],[0.807,0.567], [0.634, 0.245], [0.856, 0.706], [0.811, 0.524], [0.825, 0.684], [0.842, 0.715], [0.753, 0.68]]
y = [[5], [7], [8], [8], [8], [7], [10], [6], [7], [8], [10], [6], [8], [7], [5], [9], [7], [9], [8], [8]]
model = LinearRegression()
model.fit(X, y)
X_test = [[0,0],[1,0],[0,1]]
y_test = [[90],[90],[90]]
predictions = model.predict(X_test)
for i, prediction in enumerate(predictions):
    print('Predicted: %s, Target: %s' % (prediction, y_test[i]))
print('R-squared: %.2f' % model.score(X_test, y_test))

