list1 = [int(x) for x in input("Enter List Elements Seperated By Space : ").split()]
rotate1 = input("Rotate By : ")
rotate1 = int(rotate1)
if rotate1 > 0 :
    rotate1 = rotate1%len(list1)
    for i in range (0,rotate1):
        t = list1[-1]
        list1.pop()
        list1.insert(0,t)
    print(list1)
else :
    print(list1)
