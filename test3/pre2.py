f=open('gps1.txt','r')
g=open('track.txt','w')
list = []
for line in f.readlines():
    list.append(line)
for i in range(50):
    for j in list:
        if int(j.split()[0])==i:
            str=j.split()
            str[1]=''
            str[6]=''
            str[5]=''
            g.write(' '.join(str))
            g.write("\n")
f.close()
g.close()
