responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Where would be your dream vacation? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat != 'yes':
        polling_active = False
  

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + "'s dream vacation is to go to " + response + ".")
