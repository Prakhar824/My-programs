l=[1,2,3,4]
m=[]
n=[]
for i in range(3,-1,-1):
    m.append(l[i])
for i in range(0,4):
    n.append(l[i]+m[i])
    
print(n)