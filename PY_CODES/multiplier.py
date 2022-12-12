"""
This code take the even numbers and return the total value
"""
numbers = [8,9,11,20,32,101,100] 
    

def multiply_even_numbers (even):
    total = 1
    for num in numbers:
            if num % 2 == 0:
                total = total * num
    return total

    #MAIN
try:    
    total = multiply_even_numbers(numbers)
    print(f"the total is : {total}")
except Exception as error:
    print(f"check out the : {error}")    



