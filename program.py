print(">>>>>>>>>> Rock, Paper, Scissors <<<<<<<<<<<<<<<<")
import random
def game():
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)
    print("Computer has choosen::", computer)
    if (user==computer):
        print("Its a Draw!!!  No Points to Both User and Computer.")
        print(".........................................")
    elif(user=="rock"and computer=="scissors"):
        print("User gets one point!!!")
        print(".........................................")
    elif(user=="Paper"and computer=="rock"):
        print("User gets one point!!!")
        print(".........................................")
    elif(user=="scissors" and computer=="paper"):
        print("User gets one point!!!")
        print(".........................................")
    elif(user=="scissors"and computer=="rock"):
        print("Computer gets one point!!!")
        print(".........................................")
    elif(user=="rock"and computer=="paper"):
        print("Computer gets one point!!!")
        print(".........................................")
    elif(user=="paper" and computer=="scissors"):
        print("Computer gets one point!!!")
        print(".........................................")
    else:
        print("Invalid option")
        print(".........................................")
user= input("Enter your choice rock, paper, scissors:: ")
game()






