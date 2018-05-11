condition=1
break_var = False
while(1):
	print("outside loop running")
	while(1):
		while(1):
			while(1):
				print("inside")
				condition += 1
				if condition > 10:
					break_var = True
					break
			if break_var == True:
				break	
		if break_var == True:
			break				
	if break_var == True:
		break