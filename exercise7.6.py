sandwiches_order = ['tuna', 'ham' , 'cheese', 'chicken' , 'salmon', 'vegie']
finished_sandwiches = []


while sandwiches_order:
    current_order = sandwiches_order.pop()

    print("I made your " + current_order.title() + " sandwich.")
    finished_sandwiches.append(current_order)

print("\nThe following sandwiches that have been made are: ")
for current_order in finished_sandwiches:
    print(current_order.title())

print(sandwiches_order)
