Maxsize=30001
def Find2(i):
    r=i
    while parent[r]>=0:
        r=parent[r]
    while i!=r :
        s=parent[i]
        parent[i]=r
        i = s
    return r
def WeightedUnion(i,j):
    temp =parent[i]+ parent[j]
    if parent[j]<parent[i]:
        parent[i]=j
        parent[j] = temp
    else:
        parent[j]=i
        parent[i]= temp
while True :
    n,m=map(int,input().split())
    if n==0 and m==0 :break
    parent=[-1]*Maxsize
    for i in range(m):
        inlist=list(map(int,input().split()))
        x=inlist[1]
        for j in range(2,inlist[0]+1):
            xroot=Find2(x)
            y=inlist[j]
            yroot=Find2(y)
            if xroot!=yroot:
                WeightedUnion(xroot,yroot)
    zeroroot=Find2(0)
    print("{0:d}".format(-parent[zeroroot]))