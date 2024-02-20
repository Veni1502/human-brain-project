#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
while True:
    
    choice = ["stone","paper","scissors"]
    win = ["don't worry I'll give you another chance If want","better luck next time"]
    lose = ["you got me this time!\nlets play another round","everyone can get lucky once!\nTry me again!"]
    
    i = 0
    computer_score = 0
    player_score = 0
    mapper = {1 : "stone",2 : "paper",3 : "scissors"}
    option = [1,2,3]
    
    def user_input():
        global computer,player
        computer = random.choice(choice)
        
        player = int(input("""1.stone,
2.paper,
3.scissors
Enter your choice:
"""))
        while True:
            if  player not in option:
                print("please enter a valid input")
                user_input()
            else:
                break
            
    

    for i in range (3):
        user_input()
        player_choice = mapper.get(player)
        print("Your choice:",player_choice)
        print("computer choice :",computer)
        
        if(computer == "stone" and player_choice == "scissors" or
              computer == "paper" and player_choice == "stone" or
              computer == "scissors" and player_choice == "paper"):
            computer_score+= 1
            
        if(player_choice == "stone" and computer == "scissors" or
              player_choice == "paper" and computer == "stone" or
              player_choice == "scissors" and computer == "paper"):
            player_score+= 1
            
    print("computer score:",computer_score)
    print("Your score:",player_score)
    
    if computer_score > player_score:
        print("computer won")
        print(random.choice(win))
    
    elif player_score > computer_score:
        print("congratulation!,You won")
        print(random.choice(lose))
        
    if computer_score == player_score:
        print("This game is a tie")
        
    play_again = input("Do you want to play this game again yes/no:")
    if play_again.lower() == "yes":
        continue
    else:
        print("Thank you for playing")
        break
        


# In[ ]:




