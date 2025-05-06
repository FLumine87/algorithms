from queue import PriorityQueue 
pq=PriorityQueue() 
while True:
    dict1=dict() 
    Msgstr=input()
    
    if Msgstr=="END":
        break
    
    Msglen=len(Msgstr)
    
    for i in range(Msglen):
        if dict1.get(Msgstr[i])!=None:
            dict1[Msgstr[i]]+=1 
        else:
            dict1[Msgstr[i]]=1
    
    for key,value in dict1.items():
        pq.put(value) 
    
    if pq.qsize()==1:
        ret=pq.get()
        print(8*ret,ret,"{0:.1f}".format(8))
        continue 
    
    blen=0
    while pq.qsize()!=1:
        temp1=pq.get()
        temp2=pq.get()
        # temp=temp1+temp2
        blen+=temp1+temp2
        pq.put(temp1+temp2)
    print(Msglen*8,blen,"{0:.1f}".format(Msglen*8/blen))
    while not pq.empty():
        pq.get()