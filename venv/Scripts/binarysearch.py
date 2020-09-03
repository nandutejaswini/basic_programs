def search(list,n):
    l = 0
    u = len(list)-1
    while l<=u:
        m=(l+u)//2
        if list[m]==n:
            return True
        else:
            if list[m]<n:
                l=m+1;
            else:
                u=m-1;
    return False
list=[2,4,6,7,8,9]
n=9
if search(list,n):
    print("found")
else:
    print("not found")
    print(" ")