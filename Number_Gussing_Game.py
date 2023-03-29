import random as rm 

top_range = input("Enter a number :")

if top_range.isdigit():
    top_range=int(top_range)

    if top_range<=0:
        print("Enter number greator than 0 next time !")
        quit()
else:
    print("Please Enter a number next time! ")
    quit()

random_number = rm.randint(0,top_range)
gusses = 0

while True:
    gusses +=1
    guess = input("Make a guess : ")
    if guess.isdigit():
        guess=int(guess)
    else:
        print("Plz enter a number")
        continue
    if guess == random_number :
        print("Your guess is correct!")
        break
    elif guess > random_number :
        print("Your guess is greator than number")
    else:
         print("Your guess is less than the number")
   
print("You got the guess in " , gusses, "time")