import psutil
import operator
conn = psutil.net_connections(kind='tcp')

print ("pid","laddr","raddr","status")
di = {}
listo = []
for a in conn:
    if (a[4] != () ):
        listi =[]
        listi.append(a[6])
        laddr = str(a[3][0])+'@'+str(a[3][1])
        listi.append(laddr)
        raddr = str(a[4][0])+'@'+str(a[4][1])
        listi.append(raddr)
        listi.append(a[5])
        listo.append(listi)
        if (di.has_key(a[6])):
            di[a[6]]+=1
        else:
            di[a[6]]=1
for b in listo:
    b.append(di.get(b[0]))
sorted_bi = sorted(di.items(), key=operator.itemgetter(1),reverse=True)
for c in sorted_bi:
    for d in listo:
        if(c[0]==d[0]):
           print '\"%d\",\"%s\",\"%s\",\"%s\"'% (d[0],d[1],d[2],d[3])
#  sorted(listo,key=operator.itemgetter(4),reverse=True)
# for c in listo :
#     print "\"",c[0],"\"",",","\"",c[1],"\"",",","\"",c[2],"\"",",","\"",c[3],"\""






