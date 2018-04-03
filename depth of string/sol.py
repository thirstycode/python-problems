inp = input("")
counterl = 0
counterr = 0
nested_counter = 0
for char in inp:
    if char == "(":
        counterl += 1
    if char == ")":
        counterr += 1
    if counterl == counterr :
        nested_counter = max(counterl,nested_counter)
        counterl = counterr = 0
print(nested_counter)
