f=open('gps.txt','r')
g=open('gps1.txt','w')
for line in f.readlines():
    line=line[6:]
    g.write(line)
f.close()
g.close()

