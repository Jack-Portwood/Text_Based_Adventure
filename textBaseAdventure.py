#Setup 
decision = ["yes", "no"]
direction = ["forwards", "backwards", "left", "right"]

#Introduction 
print(" You are travelling down a wooded road..\n an old crone waves you down...")
name = raw_input("Crone: Greetings traveler, what is your name?\n")
print( "Salutations, " +name+ ".")







#Start of Game
response = ""
while response not in decision:
    print("Crone: I need you to retrieve me my stolen diadem from the mountain Queen..")
    print("Crone: I will reward you with immeasurable wealth and fortune... ")
    response = raw_input( "Do you accept ? \n yes/no \n")
    if response == "yes":
        print("The crown speaks in tounges and with a flick of the wrist you are stood in bog at the foot of a mountain")
    else:
        print("The crown stabs you with a blunt rusty blade... you are dead.")
        quit("Game Over...\n and thus draws to its natural conclusion the tale of" +name+" the intrepid ")