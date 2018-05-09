def input1():
	array_2d = []
	for i in range(1,21):
		string = input("Enter Row : ")
		p=string.split()
		p=[int(x) for x in p]
		array_2d.append(p)
	return array_2d

x = input1()
print(x)