# this code sum up each item in the order_list and write it to a receipt file

order_list = {'tomato':30, 'thyme':4.50, 'garlic':7.5, 'rice':10, 'onions':4, 'fish':9.99}
def sales(order):
    try:
        total = 0
        with open("receipt.txt", "w") as receipt:
            for item in order_list:
                total += order_list[item]
            receipt.write(str(total))
            print(f'The total sales order is : #{total}')
    except Exception as error:
        print(f"We have an error: {error}")
        return total
        
sales(order_list)
