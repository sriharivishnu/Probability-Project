#Counter to count the total number of possible games
counter = 0
#The total probability (Should equal 1 once divided by 6. The difference is the error margin due to rounding)
totalprob = 0.0
# Probabilities of sums of 2,3,4,5,6,7,8,10,11,12
P = [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36]
#An array to count the number of times a game ended after x amount of turns
turns = [0 for x in range(13)]

# Calulating the probability that B wins with the formula
# c is the value of the central die
def PBWin(c):
    s = 0.0
    for a in range(2+c, 12+c+1):
        s += P[a-c-1-1]*(30-a)**2/900
    return s 

#Calculating the probability that A wins with the complement of the formula for B
def PAWin(c):
    s = 0.0
    for a in range(2+c, 12+c+1):
        s += P[a-c-1-1]*(1-(30-a)**2/900)
    return s 
"""
Since the game tree is a tree, you can recurse on each node. Return when the lives of a player equals 0. Return the probability of B winning in that state.
If Player A has 0 lives left, increase the counter for number of possible games by 1, increase the total probability by the amount to get to that point in the tree.
Also, increase the count of the total turns it took to get there. Same for Player B.
If neither player has 0 lives, recurse to the next level of the tree and add the probability of B winning from each branch.

NOTE: prev stores the specific order of players who have lost lives. Therefore adding A onto the path means finding the probability that B wins.
"""
def recurse(prev, startlives, livesa, livesb, prob):
    global counter
    global totalprob
    if (livesa == 0):
        # print ("B wins with: " + " ".join(prev) + " and with probability " + str(prob))
        counter += 1
        totalprob += prob
        turns[len(prev)]+=prob/6
        return prob #Return the probability of the current branch since the B won this branch
    elif (livesb == 0):
        # print ("A wins with: " + " ".join(prev) + " and with probability " + str(prob))
        counter += 1
        totalprob += prob
        turns[len(prev)]+=prob/6
        return 0
    else:
        return recurse(prev + ["A"], startlives, livesa-1, livesb, prob*PBWin(startlives)) + recurse(prev + ["B"], startlives, livesa, livesb-1, prob*PAWin(startlives))

#Start the process of recursing by considering the two branches (Player A losing first, or Player B losing first)
def start(lives):
    #P(B winning | center dice is lives)
    return recurse(["A"], lives, lives-1, lives, PBWin(lives)) + recurse(["B"], lives, lives, lives-1, PAWin(lives))

p = []
probability = 0.0
#Go through all the possible centre dice rolls (1-6)
for x in range(1,7):
    #P(A|rolled x as centre die)
    probability += (1/6)*start(x)
    
print (counter)
print (1-totalprob/6)
print ("A wins with probability: ", 1-probability)
print ("B wins with probability: ", probability)

print (turns, sum(turns))

