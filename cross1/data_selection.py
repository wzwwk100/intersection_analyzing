f = open('test.rou.xml','r')
g = open('selected_trips.txt','w')
list = []
list2 = []
for line in f.readlines():
    list.append(line)
str = raw_input("target:")
for i in range(len(list)):
    if list[i].find(str) != -1:
        target_num = list[i-1].split()[1][4:len(list[i-1].split()[1])-1]
        list2.append(int(target_num))
        print (target_num)
        g.write(list[i-1])
        g.write(list[i])
        g.write("\n")
f.close()
g.close()

f = open('track.txt','r')
g = open('selected_trace.txt','w')
list3 = []
for line in f.readlines():
    list3.append(line)
for i in list2:
    for j in list3:
        if int(j.split()[0]) == i:
            g.write(j)
    g.write("\n")
f.close()
g.close()
