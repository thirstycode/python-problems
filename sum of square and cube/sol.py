x = input("Enter A Number : ")
x = int(x)
for i in range(int(int(x)**(0.25)),int(int(x)**(1/3)) + 1):
    if  i*i + i*i*i == x :
        print (str(i) + "**2 + " + str(i) + "**3 = " + str (x))
