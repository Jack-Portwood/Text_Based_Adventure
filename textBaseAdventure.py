#Setup 
decision = ["yes", "no"]
direction = ["forwards", "backwards", "left", "right"]

#Introduction 
print(" You are travelling down a wooded road..\n an old crone waves you down...")
name = raw_input("Crone: Greetings traveler, what is your name?\n")
print( "Salutations, " +name+".")

#Start of Game
response = ""
while response not in decision:
    print("Crone: I need you to retrieve me my stolen diadem from the mountain Queen..")
    print("Crone: I will reward you with immeasurable wealth and fortune... ")
    response = raw_input( "Do you accept ? \n yes/no \n")
    if response == "yes":
        print("The crown speaks in tounges and with a flick of the wrist you are stood in bog at the foot of a mountain\n")
    else:
        print("The crown stabs you with a blunt rusty blade... you are dead.")
        quit("Game Over...\n and thus draws to its natural conclusion the tale of " +name+ " the intrepid ")

#Level One 
response = ""
while response not in direction:
    print("You stand look towards a great mountain.. your old leather boots begin to let in the foul smelling water of the bog\n")
    print("Directly in front of you bog and the mountain.. \n")
    print("To your right in the distance there is what appears dead forest.. \n")
    print("To your left in the deistance there is a rise in the ground.. \n")
    print("Behind you lies bog as far as the eye can see..\n")
    response = raw_input("Which direction do you choose? \n forwards \n backwards \n right \n left\n ")
    if response == "forwards":
        print(""+name+ " trudged through the dank bog for days, the mountain did no appear any closer," +name+ "succumb to exhaustion and was consumed by the bog.")
        quit("Game Over...\n and thus draws to its natural conclusion the tale of " +name+ " the intrepid ")

    elif response == "backwards":
        print(""+name+ " trudged through the dank bog for days," +name+ "succumb to exhaustion and was consumed by the bog.")
        quit("Game Over...\n and thus draws to its natural conclusion the tale of "  +name+ " the intrepid ")
