prompt ="\nTell me your age to find our the cost of your movie ticket: "
prompt +=  "\nEnter 'quit' when you are finished. "

while True:
    
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    

    if age < 3:
        print("\nYou may enter for free")
    elif age <13:
        print("\nThe cost of the ticket is £10")
        
    else:
        print("\nThe cost of the ticket is £15")
