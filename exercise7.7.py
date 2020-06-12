sandwiches_order = ['tuna', 'pastrami','ham' ,
                    'cheese','pastrami', 'chicken' ,
                    'pastrami','salmon', 'vegie']
finished_sandwiches = []

print("Deli has ran out of Pastrami.")

while 'pastrami' in sandwiches_order:
    sandwiches_order.remove('pastrami')

while sandwiches_order:
    current_order = sandwiches_order.pop()

    print("\nI made your " + current_order.title() + " sandwich.")
    finished_sandwiches.append(current_order)

print("\nThe following sandwiches that have been made are: ")
for current_order in finished_sandwiches:
    print(current_order.title())

print(sandwiches_order)
