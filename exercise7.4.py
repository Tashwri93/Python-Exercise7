toppings = "\nTell me which toppings you would like on your pizza: "
toppings += "\nEnter quit when that is enough."



while True:
    
    message = input(toppings)
    

    if message == 'quit':
        break
    else:
        print("You'll add that to your toppings " + message)
