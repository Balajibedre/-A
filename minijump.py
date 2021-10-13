def jump(self, A):
    l = len(A)
    count = 0
    pos = 0
    for i in range(1,l):
        A[i] = max(i+A[i], A[i-1])
    while(pos < l-1):
        if(pos >= A[pos]):
            return - 1
        if(pos < A[pos]):
            count+=1
            pos = A[pos]
    return count
