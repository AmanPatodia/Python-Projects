import random

usercount = 0
computercount = 0
options = ["rock","paper","sessior"]

while True:
    user_input = input("Enter Rock/Paper/Sessior or Q to Quit the game: ").lower()

    if user_input == "q":
        break

    if user_input not in options :
        continue

    random_number = random.randint(0,2)
    computer_picked = options[random_number]
    print("Computer picked",computer_picked,".")

    if user_input =="rock" and computer_picked =="sessior":
        print("You wins! ")
        usercount+=1
    elif user_input=="paper" and computer_picked=="rock" :
        print("You wins!")
        usercount+=1
    elif user_input=="sessior" and computer_picked=="paper":
        print("You wins!")
    elif ((user_input=="rock" and computer_picked=="rock") or (user_input=="sessior" and computer_picked=="sessior") or (user_input=="paper" and computer_picked=="paper")) :
        print("NO one wins!")
    else:
        print("You lost!")
        computercount+=1
    
print("You won",usercount,"times.")
print("Computer won",computercount,"times.")
print("Goodbye")
        