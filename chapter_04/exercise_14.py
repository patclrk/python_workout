MENU = {'sandwich': 10, 'chianti': 12, 'primitivo': 15, 'montepulciano': 20, 'lambrusco': 13}

'''
Prompts user for order
If user enters item from const MENU, display item and running total
If user input not in dict, display warning and continue
If user input is null, break and display final total
'''
def restaurant():
    order_total = 0

    while True:
        user_input = input('Order: ')
        if user_input:
            if user_input in MENU:
                order_total += MENU[user_input]
                print(f'{user_input} is {MENU[user_input]}, total is {order_total}')
            else:
                print(f'Sorry, we\'re fresh out of {user_input}')
        else:
            break
    
    print(f'Your total is {order_total}')

if __name__ == "__main__":
    restaurant()


# book solution notes

# null check:
#   'if not user_input'
# .strip() on input