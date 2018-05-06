# <------lcm of first n digits------>

# find gcd of two numbers
def find_gcd(a,b):
	gcd = 1
	big = max(a,b)
	small = min(a,b)
	for i in range(2,small+1):
		if big%i == 0 and small%i==0:
			gcd = max(i,gcd)
	return gcd

# find lcm of two numbers recursively
# used the fact that lcm(a,b,c,d,e) = lcm(a,lcm(b,lcm(c,lcm(d,e))))
def find_lcm(num,num2):
	if num2 == "start":
		lcm_last = num*(num-1)/find_gcd(num,num-1)
		return find_lcm(num-2,lcm_last)
	else:
		lcm_last = num*num2/find_gcd(num,num2)
		if num == 1:
			return num2
		else:
			return find_lcm(num-1,lcm_last)

# to call the function from single argument
def find_answer(num):
	return find_lcm(num,'start')

print("This calculates lcm of first n digits!")
number = input("Enter number to which lcm needs to be find: ")

print("Lcm of digits from 1 to " + str(int(number))+ " is " + str(int(find_answer(int(number)))))