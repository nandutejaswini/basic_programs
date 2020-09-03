def bubblesort(list):
    for j in range(len(list)-1,0,-1):
        for i in range(j):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp


list=[5,3,17,4,18,9]
bubblesort(list)
print(list)