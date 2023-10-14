import random
while True:
    choices=["rock",'paper','scissors']
    player=None
    computer=random.choice(choices)
    while player not in choices:
        player=input("rock,paper scissors?: ").lower()

    if player==computer:
      print("Computer:",computer)
      print("Player: ",player)
      print("TIE")
    elif player=="rock":
      if computer=="paper":
         print("Computer:",computer)
         print("Player: ",player)  
         print("You lose")
      if computer=="scissors":
        print("Computer:",computer)
        print("Player: ",player)  
        print("You win")
    elif player=="scissors":
      if computer=="rock":
         print("Computer:",computer)
         print("Player: ",player)  
         print("You lose")
      if computer=="paper":
        print("Computer:",computer)
        print("Player: ",player)  
        print("You win")
    elif player=="paper":
      if computer=="scissors":
         print("Computer:",computer)
         print("Player: ",player)  
         print("You lose")
      if computer=="rock":
        print("Computer:",computer)
        print("Player: ",player)  
        print("You win")
    play_again=input("Play again?:(yes/no): ").lower()

    if play_again!="yes":
       break
