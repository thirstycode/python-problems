list1 = [int(x) for x in input().split()]
rotate1 = input("")
rotate1 = int(rotate1)
if rotate1 > 0 :
    rotate1 = (rotate1)%len(list1) - 1
    list1 = list1[rotate1:] + list1[:len(list1)-rotate1-1]
    print(list1)
else :
    print(list1)
