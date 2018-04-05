x = input("Enter A Number : ")
x = int(x)
for i in range(1,int(x)):
    p = i*i*i
    for j in range(1,int(x-p)):
        if j*j == x-p:
            print(str(j) + "**2 + " + str(i) + "**3 = " + str(x) )
