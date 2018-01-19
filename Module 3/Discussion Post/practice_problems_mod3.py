"""First Excercise"""
# Sandwich Orders List and Finsihed Sandwiches 
sandwich_orders = ["Bologna Sandwich", "Chicken Parmesean Hero", "Roast Beef Sandiwch", "Pulled Pork Taco", "Bagel with Creamcheese"]
finished_sandwiches = []

# Make All Sandwiches and Loop/Append All Sandiwches to the finished_sandwiches variable
for sandwich in sandwich_orders:
    print("I have made your {0}".format(sandwich))
    finished_sandwiches.append(sandwich)

#Seperator
print("\n------------------------\n")

for finished_sandwich in finished_sandwiches:
    print("We hope you enjoy your {0} from Eric's Sandwich Shop!".format(finished_sandwich))
    
    
    
    
    
"""Second Excercise"""
print("\n\n---------------------Second Exercise----------------\n")
sandwich_orders = ["Bologna Sandwich", "Pastrami Sandwich", "Chicken Parmesean Hero", "Pastrami Sandwich", "Roast Beef Sandiwch", "Pulled Pork Taco", "Bagel with Creamcheese", "Pastrami Sandwich"]
finished_sandwiches = []

# Pop Pastrami Sandwiches from the original list
print("We Do NOT have any Pastrami in stock today!\n")

for sandwich in sandwich_orders:
    if sandwich == "Pastrami Sandwich":
        sandwich_orders.pop()
    else:
        finished_sandwiches.append(sandwich)

# Loop over finished Sandwiched without Pastrami
for finished_sandwich in finished_sandwiches:
    print("Enjoy your {0}! Sorry we did not have any Pastrami in stock today. Next time :)".format(finished_sandwich))