
#i added creativity 

def menu():
    print('\nPlease select one of the following: ')
    print('1.Add item')
    print('2.View cart')
    print('3.Remove item')
    print('4.Compute total')
    print ('5.Quit' )

def additem(items, prices):
    itemname = input('What item would you like to add? ')
    itemprice = float(input(f"What is the price of the '{itemname}? $"))
    items.append(itemname)
    prices.append(itemprice)
    print(f"'{itemname}' has been added to the cart.")

def displaycart(items, prices):
    print('\nThe contents of the shopping cart are: ')
    for i in range (len(items)):
        print(f"{+1}. {items[i]} - ${prices[i]:.2f}")

def removeitems(items, prices):
    try:
        itemnumber = int(input('Which item would you like to remove? ')) - 1
        if 0 <= itemnumber < len(items):
            del items[itemnumber]
            del prices[itemnumber]
            print('Item removed.')
        else:
            print('Sorry, that is not a valid item number. ')
    except ValueError:
        print('Invalid input. Please enter a valid item number.')

def computetotal(prices):
    totalprice = sum(prices)
    print(f'\n The total price of the items in the shopping cart is ${totalprice:.2f}')


    

def welcome():
    print('Welcome to the Shopping Cart Program! ')

    items = []
    prices = []

    while True:
        menu()
        chioce = input('Please enter an action: ')

        if chioce == '1':
            additem(items, prices)
        elif chioce == '2' :
            displaycart(items, prices)
        elif chioce == '3':
            removeitems(items, prices)
        elif chioce == '4':
            computetotal(prices)
        elif chioce == '5':
            print('Thank you. Goodbye')
            #creativity
            import time
            time.sleep(1)
            print('💖💖💖💖💖💖   💖💖💖💖💖💖\n \
                  💖💖💖💖💖💖💖💖💖💖💖💖💖💖💖💖💖\n\
                     💖💖💖💖💖💖💖💖💖💖💖💖💖💖💖\n\
                        💖💖💖💖💖💖💖💖💖💖💖💖💖\n\
                            💖💖💖💖💖💖💖💖💖💖\n\
                               💖💖💖💖💖💖💖💖\n\
                                  💖💖💖💖💖💖\n\
                                      💖💖💖💖\n\
                                         💖💖')

            break
        else:
            print('Invalid Choice. Please choose a valid option.')

if __name__ == "__main__":
    welcome()