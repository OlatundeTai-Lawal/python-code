# using range method to append a number to print the maximum and minimum
my_numbers = []
for x in range(4):
    x = input('enter a number :')
    my_numbers.append(x)   
if x == '' :   
    print("None or []")
else:
    print(f"{max(my_numbers)} {min(my_numbers)}")