#This is mt first project on Cafe/Restaurant Management System......


menu = {
    'Pizza':260,
    'Pasta':60,
    'Burger':40,
    'Coffee':30,
    'Maggie':40,
    'Sandwich':50,

}
print("welcome to varsha's restaurant")
print('Pizza:Rs260\n Pasta:Rs60\nBurger:Rs40\nCoffee:Rs30\nMaggie:Rs40\nSandwich:RS50')

order_total=0
item1=input('Enter the name of the item you want to order:')
if item1 in menu:
    order_total += menu[item1]
    print(f'Your item {item1} has been added to your order ')

else:
    print(f'Sorry! , This item is not available')

another_item=input("Do you want to add another item (Yes/No)")        
if another_item=='Yes':
    item2=input('Enter the name of the second item you want to order:')
    if item2 in menu:
        order_total += menu[item2]
        print(f'Your item {item2} has been added to your order ')

    else:
        print(f'Sorry! , This item is not available')

print(f'The total amount of items  to pay is {order_total}')


print("HAVE A GOOD DAY")