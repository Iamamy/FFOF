# you can use print for debugging purposes, e.g.
# print "this is a debug message"
# you can use print for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    B = [0]*(N+1)
    if len(A)<1:
        return 1
    
    for n in xrange(N):
        if A[n]>0 and A[n]<=N:
            B[A[n]-1]=1
    
    for k in xrange(N+1):
        if B[k]==0:
            return (k+1)
    
    return (k+1)

print(solution([-1,6,4,3,2]))
    
