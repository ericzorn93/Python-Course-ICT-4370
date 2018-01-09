# First Exercise: Print Names
names = ["Matt", "Lauren", "Nick", "Tim", "Nate", "Elana"]

print("First Exercise")
for val, name in enumerate(names):
    print(val, name)


# Second Exercise: Greeting Message
print("\nSecond Exercise")
for name in names:
    print("Hey {0}, nice to meet you today! How are you?".format(name))



# Third Exercise: Person I would like to invite to dinner
print("\nThird Exercise")
dinner_guest_list = ["Eddy Zorn", "Barry Spector", "Phil Mickelson"] # Eddy and Barry are both of my grandfathers. Phil Mickelson is a famous golfer.

for guest in dinner_guest_list:
    print("Dear {0}, I am throwing a dinner party at my house this weekend on Saturday evening. I would really appreciate it if you could come.".format(guest))


# Fourth Exercise: Change Guest List
print("\nFourth Exercise")
print("Unfortunately, {0} cannot make it to the dinner party this weekend".format(dinner_guest_list[2]))
dinner_guest_list.pop() # Delete Phil Mickelson from the List
dinner_guest_list.append("Bubba Watson") # Add Bubba Watson (Another Golfer) to the list
# Loop over new guest list for the dinner guests
for new_guest in dinner_guest_list:
    print("We have had a change in attendees for this weekend's dinner party. We still would like to extend the invite to you, {0}, this weekend for the party.".format(new_guest))


# Fifth Exercise: Username Testing
print("\nFifth Exercise")
current_users = ["bobby123", "superheroes_rock", "rockandrollfan321", "elaineSmith912"]
new_users = ["superHeroes_rock", "coding_fan", "pythonprogrammer100", "BOBBY123", "dogLover"]

for user in new_users:
    if user.lower() in current_users:
        print("{0} is already a taken username! You need to pick a new one.".format(user))
    elif user.upper() in current_users:
        print("{0} is already a taken username! You need to pick a new one.".format(user))
    else:
        print("{0} is an available username. Good choice!".format(user))

print("\n") #Space for legibility



exit() # Quit Program