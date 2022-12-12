print('***********This code is to calculate input by usre\n*****')
def add (a, b):
    total = num_1 + num_2
    print(f"{num_1} + {num_2} is {total}") 
    return total
    
def substract (a, b):   
    total = num_1 - num_2
    print(f"{num_1} - {num_2} is {total}") 
    return total 
	
def multiply (a, b):
    total = num_1 * num_2
    print(f"{num_1} * {num_2} is {total}") 
    return total 
	    
def division (a, b):
    total = num_1 / num_2
    print(f"{num_1} / {num_2} is {total}") 
    return total
	    
def exponetial (a, b):
    total = num_1 ** num_2
    print(f"{num_1} ** {num_2} is {total}") 
    return total
	    
def modulo(a,b):
    total = num_1 % num_2
    print(f"{num_1} % {num_2} is {total}")
    return total 
	    
	    
def integer_division(a,b):
    total = num_1 // num_2
    print(f"{num_1} // {num_2} is {total}") 
    return total	           
		
calculator_operator = ["+", "-", "*", "/", "**", "%", "//"]
print([calculator_operator])
while True:
    operators = input("select operator of choice for calculator\n")
    if operators in calculator_operator:
        num_1 = int(input("1st numbers from user 1\n"))
#operators = input("select your operator\n")
        num_2 = int (input("2nd number from user 2\n"))
        if operators == "+":
            add(num_1, num_2)
        elif operators == "-":
            substract(num_1,num_2) 
        elif operators == "*": 
            multiply(num_1,num_2)
        elif operators == "/":
            division(num_1,num_2)
        elif operators == "**":
            exponetial(num_1,num_2)
        elif operators == "%":
            modulo(num_1,num_2)
        elif operators == "//":
            integer_division(num_1,num_2)
        choice = input("exit or proceed?: \n").lower()
        if choice == "exit":
            break
    else: 
        print("operator not found")
               
               
                      

