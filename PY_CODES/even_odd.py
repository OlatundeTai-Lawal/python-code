print("This def funtion to print even and odd numbers\n")

def even_odd_fct(number):
    if number % 2 == 0: 
        print(f'{number} is even')
    else: 
        print(f'{number} is odd')
number1 = int(input("enter your number:\n"))       

even_odd_fct(number1)