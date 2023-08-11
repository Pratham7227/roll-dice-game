import  random
li=[]
dict={}
numberOfPlayers=int(input("how many players want to play this game:"))
index=1
while(numberOfPlayers>0):
    player = input(f"Add player {index}:")
    li.append(player)
    index+=1
    numberOfPlayers-=1

for player in li:
    print(f"{player} you turn")
    userScore = 0
    while (True):
        userInput = input("what do you want to do roll the dice or leave the game {roll,quit}:")
        if (userInput.lower() == "roll"):
            thereIsCatch = input("If you get 1 then you lose the game you are sure to play {yes,no}: ")
            if (thereIsCatch.lower() == "yes"):
                rolldice = random.randrange(1, 6)
                print(("rolling...."))
                print(rolldice)
                if (rolldice == 1):
                    print("Sorry uou lose the game")
                    userScore = 0
                    print("Thank you your score is:", userScore)
                    dict[player]=userScore
                    break
                else:
                    userScore += rolldice
            else:
                print(f"you Quit the game and  your score is:{userScore}")
                dict[player] = userScore
                break

        else:
            print("Thank you your score is:", userScore)
            dict[player] = userScore
            break



print(dict)
Key_max = max(dict, key = dict.get)
print(f"the winner is {Key_max}") 