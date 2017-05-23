from sklearn.linear_model import LinearRegression
X = [[0.7001,0.9712],[0.5991,0.941],[0.2932,0.7443],[0.654,0.9322],[0.66,0.868],[0.8641,0.9514],[0.5679,0.6131],[0.0831,0.9359],[0.20193,0.963891],[0.781737,0.864407],[0.359317,0.910833],[0.681514,0.933677],[0.926503,0.778187]]
y = [[103], [95], [92], [124], [94], [114], [73], [63], [72], [128], [78], [126],[105]]
model = LinearRegression()
model.fit(X, y)
X_test = [[0,0],[1,0],[0,1]]
predictions = model.predict(X_test)
for i, prediction in enumerate(predictions):
    print('Predicted: %s' % (prediction))

print "Predicted Speed"
print 1500/(predictions[1]-predictions[0])
print "Average Speed"
print "25.055679287305122"
print "Accuracy Rate"
print 1500/(predictions[1]-predictions[0])/25.056
print "Predicted Speed"
print 1500/(predictions[2]-predictions[0])
print "Average Speed"
print "24.871039056742815"
print "Accuracy Rate"
print 1500/(predictions[2]-predictions[0])/24.871
