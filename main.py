# import necessary functions
from IPython.display import clear_output

# global list variable
cart = []
value_cart = []

# create function to add items to cart
def addItem(item, cost):
    clear_output()
    cart.append(item)
    value_cart.append(cost)
    print('{} has been added.'.format(item))
    print('${} is the price of the added item'.format(cost))

# create function to remove items from cart
def removeItem(item):
    clear_output()
    try:
        if item.isdigit():
            item_removed = cart.pop(int(item) - 1)
            value_cart.pop(int(item) - 1)
            print('{} has been removed.'.format(item_removed))
        else:
            cart.remove(item)
            value_cart.pop(cart.index(item))
            print('{} has been removed.'.format(item))
    except:
        print('Sorry we could not remove that item.')
        
# create function to show items in cart
def showCart():
    clear_output()
    if cart:
        print('Here is your cart:')
        for i in range(len(cart)):
            print('{}) {}'.format(i + 1, cart[i]) + "........."  + "$" + value_cart[i]) 
    else:
        print('Your cart is empty.')

# create function to clear items from cart
def clearCart():
    clear_output()
    cart.clear()
    value_cart.clear()
    print('Your cart is empty.')

def total_amount():
    total = 0
    for j in range(len(value_cart)):
        total = total + int(value_cart[j])
    print("Your total is: " + "$" + str(total)) 
    return total
# create main function that loops until the user quits

def check_validity(num):                                                   # this function adds every digit of the card number to a list and,
    validlist=[]
    credit_check = False
    #while not credit_check:
    for i in num:
        validlist.append(int(i))
    for i in range(0,len(num),2):                                             # applying Luhn Algorithm to check whether resulting sum is divisible by ten
        validlist[i] = validlist[i] * 2
        if validlist[i]  >= 10:
            validlist[i] =  (validlist[i]//10 + validlist[i]%10)
    
    if sum(validlist)% 10 == 0:
        credit_check = True
        print("This is a VALID CARD!")
        return credit_check
    
    else:
        credit_check = False
        print('INVALID CARD NUMBER')
        return credit_check

def cardnumber():                                                                     # accepts card number as a string

    n = ''
    while True:
        try:
            n = input('Enter your 16 digit credit card number : ')

            if not (len(n) == 16) or not type(int(n) == int) :
                raise Exception

        except Exception:    
            print('That is not a valid credit card number. \nMake sure you are entering digits not characters and all the 16 digits.')
            continue

        else:
            break


    return n

def billing():
    total_val = 0

    # create a company name and information
    company_name = "Straight Outta The Himalayas"
    company_address = '27 Franklin St.'
    company_city = 'Boston, MA'

    # declare ending message
    message = 'Thanks for shopping with us today!'

    # create a top border
    print('*' * 50)

    # print company information first using format
    print('\t\t{}'.format(company_name.title()))
    print('\t\t{}'.format(company_address.title()))
    print('\t\t{}'.format(company_city.title()))

    # print a line between sections
    print('=' * 50)

    # print out header for section of items
    print('\tProduct Name\tProduct Price')
    # create a print statement for each item
    for z in range(len(cart)):
        print('\t{}\t\t${}'.format(cart[z].title(), value_cart[z]))
    #print('\t{}\t${}'.format(p2_name.title(), p2_price))
    #print('\t{}\t\t${}'.format(p3_name.title(), p3_price))

    # print a line between sections
    print('=' * 50)

    # print out header for section of total
    print('\t\t\tTotal')

    # calculate total price and print out
    for j in range(len(value_cart)):
        total_val = total_val + int(value_cart[j])
    total_val = str(total_val)
    print('\t\t\t${}'.format(total_val))

    # print a line between sections
    print('=' * 50)

    # output thank you message
    print('\n\t{}\n'.format(message))

    # create a bottom border
    print('*' * 50)

def main():
    done = False
    
    while not done:
        ans = input('\nquit/add/remove/show/clear: ').lower()
        
        # base case
        if ans == 'quit':
            print('Thanks for using our program.')
            showCart()
            done = True
            if total_amount() != 0:
                num = cardnumber()
                if check_validity(num) == True:
                    billing()
        elif ans == 'add':
            item = input('What would you like to add? ').title()
            cost = input('Enter the cost of the item? ')
            addItem(item, cost)
        elif ans == 'remove':
            showCart()
            item = input('What item would you like to remove? ').title()
            removeItem(item)
        elif ans == 'show':
            showCart()
        elif ans == 'clear':
            clearCart()
        else:
            print('Sorry that was not an option.')

with open('README.txt', 'r') as RD:
    holder = RD.read()

print(holder)
main()       # run the program


