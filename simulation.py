import random

awin = 0
bwin = 0
turncount = [0 for x in range(12)]

#Roll a singular 6-sided die
def roll_die():
    return float(random.randint(1,6))

#Obtain a random real-number measurement ranging from 0 to 30
def get_random_value():
    return 30*random.random()


print ("\n\n__________STARTING PROCESS__________\n\n")

#Play the game this many times
EPOCHS = 5001
for x in range(EPOCHS):
    central_dice_val = roll_die()
    a_lives = central_dice_val
    b_lives = central_dice_val
    turns = 0
    while (a_lives > 0 and b_lives > 0):
        roller_dice_sum = roll_die() + roll_die()
        random_measured_value = abs(get_random_value() - get_random_value())
        turns += 1
        if (random_measured_value > roller_dice_sum + central_dice_val):
            # print ("Player A Lost a Life since", random_measured_value, "is greater than", roller_dice_sum + central_dice_val)
            a_lives -= 1
        else:
            # print ("Player B Lost a Life since", random_measured_value, "is less than", roller_dice_sum + central_dice_val)
            b_lives -= 1
        
    if (a_lives == 0):
        # print ("B won with " + str(b_lives) +" lives left")
        bwin += 1

    if (b_lives == 0):
        # print ("A won with " + str(a_lives) +" lives left")
        awin += 1
    
    turncount[turns] += 1

    if (x % 10 == 0 and x != 0):
        print (bwin/x)

print ("\n\n__________FINISHED PROCESS__________\n\n")

print ("Player A won", awin, "times for a total probability of", awin/EPOCHS)
print ("Player B won", bwin, "times for a total probability of", bwin/EPOCHS)

print ("NUMBER OF TURN PROBABILITIES: ")
for x in list(map(lambda x: x/EPOCHS, turncount)):
    print (x)
