#Setup 
decision = ["yes", "no"]
direction = ["forwards", "backwards", "left", "right"]
attack = ["thrust", "slash"]

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
    response = raw_input("Which direction do you choose? \n forwards \n right \n left\n ")
    if response == "forwards":
        print(""+name+ " trudged through the dank bog for days, the mountain did no appear any closer," +name+ "succumb to exhaustion and was consumed by the bog.")
        quit("Game Over...\n and thus draws to its natural conclusion the tale of " +name+ " the intrepid ")
    elif response == "backwards":
        print(""+name+ " trudged through the dank bog for days," +name+ "succumb to exhaustion and was consumed by the bog.")
        quit("Game Over...\n and thus draws to its natural conclusion the tale of "  +name+ " the intrepid ")
    elif response == "left":
        print("You walk to the point of exhaustion but you make it to the rised ground.. you pass out..")
    elif response == "right":
        print("You make it to the dead trees... the ground becomes boggier and boggier, you are consumed by the bog")
        quit("Game Over...\n and thus draws to its natural conclusion the tale of "  +name+ " the intrepid ")


#Dream 
print("Crone: I used to be the Princess of these once far lands.. but that wicked Queen took my throne.. please help restore my youth and lands.")
print("You awaken!")

#Level Two
response = ""
while response not in decision:
    response = raw_input("You bring yourself to your feet..\n you notice a man whole.. do you decend into the darkness \n yes/no \n")
if response == "yes":
    print("You climb down the ladder into the darkness....")
else:
    print("You await the author the write something......")
    quit("Game Over...\n and thus draws to its natural conclusion the tale of "  +name+ " the intrepid ")

response = ""
print("stood in the darkness and the bottom on the sharft you see nothing but darkness.. and can hear the dripping of water from the bog above\n")
while response not in decision:
    response = raw_input(" Do you light a torch and proceed \nyes/no\n")
if response == "yes":
    print ("You ignite a torch and are istanly inguled by bats you bolt down the tunnel till you begin to see light!")
elif response == "no":
    print"You carfully edge your way down the tunnel pressing your hand against the wall to guide yourself... it take agggggggees!\n you eventually see a light!"


#Mountain Queens Layer lv3
response = ""
while response not in direction:
    print("You peer from the darkness into a vast cavern..\n you relise you are in the hart of the mountian, before you on a garnit plinth.\n elumiated by a single ray of light, lies the Crones diadem..\n ")
    print("Do race forward grab it a try escape?\n")
    print("Do edge round to the room hugging the wall to the left?\n")
    print("Do edge round to the room hugging the wall to the right?\n")
    response = raw_input("How do you enter the room? \n forwards \n right \n left\n ")
if response == "forwards":
    print("as you emerge fromt he passage way a thunderous cackle erupts...\n")
elif response == "left":
    print("as you emerge fromt he passage way a thunderous cackle erupts...\n")
elif response == "right":
    print("as you emerge fromt he passage way a thunderous cackle erupts...\n")





