from sklearn.linear_model import BayesianRidge, LinearRegression
f = open('data.txt', 'r')
g = open('result.txt', 'w')
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
    k2 = y2 / 0.0135653
    X.append([k2])
    y.append(num_time2 - num_time1 - 61.697 * k1)

model = BayesianRidge(compute_score=True)
for i in range(1 , len(X)):
    print i
    model.fit(X[0:i+1], y[0:i+1])
    X_test = [[0],[1]]
    predictions = model.predict(X_test)
    print('Predicted: %s' % (predictions[0]))
    print('Predicted: %s' % (predictions[1]-predictions[0]))
    print 1500/(predictions[1]-predictions[0])
    ac_rate = 1500/(predictions[1]-predictions[0]) / 24.31259
    if ac_rate < 0 :
        ac_rate = 0
    if ac_rate > 1 :
        ac_rate = 1 / ac_rate
    print ac_rate
    g.write(str(i))
    g.write('\n')
    g.write('Predicted_time1: %s' % (predictions[0]))
    g.write('\n')
    g.write('Predicted_time2: %s' % (predictions[1]-predictions[0]))
    g.write('\n')
    g.write('Predicted_speed: %s' % (1500/(predictions[1]-predictions[0])))
    g.write('\n')
    g.write('Accuracy Rate: %s' %  (ac_rate))
    g.write('\n')
    g.write('\n')
