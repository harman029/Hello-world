# make Object of Dict
# key == item
# value == price
od = {}


while True:
    # take items from user as input
    user_input = input("Enter item with price : ")

    if not user_input:
        break
    
    #'BANANA FRIES 12'
    # use split function to get item's price value
    temp = user_input.split()
    price = temp[-1]
    
    # join rest string which is item name
    item = " ".join(temp[:-1])
    
    # Adding and updating price of the item using orderdict function 
    od[item] = od.get(item,0) + int(price)


# Printing the elements in the dictionary
for k,v in od.items():
    print (k,v)
    
    


