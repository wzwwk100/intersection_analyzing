from sklearn.linear_model import LinearRegression
X = [[0.7001,0.9712],[0.5991,0.941],[0.2932,0.7443],[0.654,0.9322],[0.66,0.868],[0.8641,0.9514],[0.5679,0.6131],[0.0831,0.9359]]
y = [[103], [95], [92], [124], [94], [114], [73], [63]]
model = LinearRegression()
model.fit(X, y)
X_test = [[0,0],[1,0],[0,1]]
predictions = model.predict(X_test)
for i, prediction in enumerate(predictions):
    print('Predicted: %s' % (prediction))

print 1500/(predictions[1]-predictions[0])
print 1500/(predictions[1]-predictions[0])/22.3
print 1500/(predictions[2]-predictions[0])
print 1500/(predictions[2]-predictions[0])/22.3
