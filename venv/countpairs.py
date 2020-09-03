cnt=0
def countpairs(lst) :
    global cnt
    for j in range(n):
        a=lst[j]
        id1=j
        id2=j
        if j==0:
            while lst[id2+1]==a:
                id2+=1
            if lst[id2+1]<=a+z and lst[id2+1]>=a-z:
                cnt+=1
        elif j<n-1:
            while lst[id2+1]==a:
                 id2+=1
            while lst[id1-1]==a:
                 id1-=1
            if (lst[id1-1]<=a+z and lst[id1-1]>=a-z) or (lst[id2+1]<=a+z and lst[id2+1]>=a-z):
                 cnt+=1
        else:
            while lst[id1-1]==a:
                id1=id1-1
            if lst[id1-1]<=a+z and lst[id1-1]>=a-z:
                cnt=cnt+1
    return cnt
n,z=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()
print(countpairs(lst))