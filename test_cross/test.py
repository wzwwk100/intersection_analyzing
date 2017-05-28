from sklearn.linear_model import LinearRegression
f = open('data.txt', 'r')
list = []
X = []
y = []
for line in f.readlines():
    list.append(line)
for i in range(len(list) / 2):
    x1 = float(list[2 * i].split()[2])
    y1 = float(list[2 * i].split()[3])
    time1 = list[2 * i].split()[1]
    num_time1 = int(time1.split(':')[0]) * 3600 + int(time1.split(':')[1]) * 60 + int(time1.split(':')[2])
    x2 = float(list[2 * i + 1].split()[2])
    y2 = float(list[2 * i + 1].split()[3])
    time2 = list[2 * i + 1].split()[1]
    num_time2 = int(time2.split(':')[0]) * 3600 + int(time2.split(':')[1]) * 60 + int(time2.split(':')[2])
    k1 = (116.30941 - x1) / (116.30941-116.2959355)
    k2 = (0 - y2) / 0.0135653
    X.append([k1,k2])
    y.append(num_time2 - num_time1)

model = LinearRegression()
model.fit(X, y)
X_test = [[0,0],[1,0],[0,1]]
predictions = model.predict(X_test)

print('Predicted: %s' % (predictions[0]))
print('Predicted: %s' % (predictions[1]-predictions[0]))
print('Predicted: %s' % (predictions[2]-predictions[0]))

print 1500/(predictions[1]-predictions[0])
print 1500/(predictions[1]-predictions[0]) / 24.31259
print 1500/(predictions[2]-predictions[0])
print 1500/(predictions[2]-predictions[0]) / 24.31019
