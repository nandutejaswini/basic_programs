num = int(input())
d = []
d1 = []
s = 0
for j in range(num):
    k = input().split()
    d.append(int(k[0]))
    d1.append(int(k[1]))
c = 1
for j in range(num):
    if s >= d[j]:
        c = c + 1
    k = min(d)
    ki = d.index(k)
    s = d1[ki] + k

    d[ki] = s
print(c, end=" ")
