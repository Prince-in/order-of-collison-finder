def swap(l, i, j,l1):#this will maintain indexlist l1 which will store position of elements in heap
    m = l1[l[i][1]]
    k = l1[l[j][1]]
    l1[l[i][1]] = k
    l1[l[j][1]] = m
    p = l[i]
    l[i] = l[j]
    l[j] = p
def checkparent(i):
    if (i-1) // 2 >= 0:
        return True
    else:
        return False
def parent(i):
    return (i-1) // 2
def heapify(l, n, i,l1):
#this is ensuring the heap below the the i
    
    min = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and l[min] > l[left] :
        min = left
    if right < n and l[min] > l[right]: 
        min = right
    if min != i:
        swap(l,i,min,l1)
        heapify(l, n, min,l1)
    return l
def heap(l,n,l1):
    for i in range(n,-1,-1):
        heapify(l,n,i,l1)
        #this will heapify the list from below

def heapup(l, i,l1):
    while checkparent(i) :
        if l[parent(i)] > l[i]:
            swap(l,i, parent(i),l1)
            i = parent(i) 

# def heapdown(l,i,l1):
#     n = len(l)
#     left = 2*i + 1
#     right = 2*i + 2
#     if left < n and l[i] > l[left] :
#         swap(l,i,left,l1)
#         i = left
#     if right < n and l[i] > l[right]: 
#         swap(l,i,right,l1)
#         i = right
def enqueue(l, data,l1):
    if len(l) == 0:
        l.append(data)
        l1[l[-1][1]] = 0
    else:
        l.append(data)
        l1[l[-1][1]] = len(l)-1
        i = len(l)-1
        heapup(l,i,l1)
def extractmin(l,l1):
    x = l[0]
    swap(l,0,len(l)-1,l1)
    l1[l[len(l)-1][1]] = -1
    l.pop()
    heapify(l,len(l),0,l1)
    return x    
def listCollisions(M, x, v, m, T):
    t = []
    res = []
    tyme = [0]*len(M)#this will store at the ith index the last collison time of ith particle
    for i in range(len(x)-1):
        if v[i+1] < v[i]:
            t.append((((x[i+1]-x[i])/(v[i]-v[i+1])), i))
    l1 = [-1] * (len(M))
    for i in range(len(t)):
        l1[t[i][1]] = i
        # this will store the index in heap of  ith particle 
    heap(t,len(t),l1)
    j = 0
    while j < m:
        if len(t) > 0:
            time = extractmin(t,l1)
            j += 1
            if time[0] > T:
                return res
            i = time[1]
            x[i] = x[i]+v[i]*(time[0]-tyme[i])
            # updating the position to ensure correct time updating
            tyme[i] = time[0]
            tyme[i+1] = time[0]
            x[i+1] = x[i]
            res.append((time[0],time[1],x[i]))
            a=v[i]
            b=v[i+1]
            v[i] = ((M[i]-M[i+1])/(M[i]+M[i+1]))*a + ((2*M[i+1])/(M[i]+M[i+1]))*b
            v[i+1] = ((2*M[i])/(M[i]+M[i+1]))*a-((M[i]-M[i+1])/(M[i]+M[i+1]))*b
            if i > 0:            
                d = v[i-1]*(time[0]-tyme[i-1])+x[i-1]                
                if v[i-1] > v[i]:
                    t1 = (x[i]-d)/(v[i-1]-v[i])
                    k = l1[i-1]
                    if k == -1:
                        enqueue(t,[t1+time[0],i-1],l1)
                    else:
                        t[k][0] = t1 + time[0]
                        if k> 1:
                            if t[(k-1)//2] > t[k] :
                                heapup(t,k,l1)
                            else:
                                heapify(t,len(t),k,l1)
                        else :
                            heapify(t,len(t),k,l1)
            if i+2<len(x):
                e = v[i+2]*(time[0]-tyme[i+2])+x[i+2]
                if v[i+1] > v[i+2]:
                    t2 = (e-x[i+1])/(v[i+1]-v[i+2])
                    k = l1[i+1]
                    if k == -1:
                        enqueue(t,[t2+time[0],i+1],l1)
                    else:
                        t[k][0] = t2 + time[0]
                        if k> 1:
                            if t[(k-1)//2] > t[k] :
                                heapup(t,k,l1)
                            else:
                                heapify(t,len(t),k,l1)
                        else:
                            heapify(t,len(t),k,l1)
        else:   
            return res
    return res

                
                
        
        
               
        
    
        
        
