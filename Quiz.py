print("Welcome to computer quiz")

playing = input("Are you ready for play! ").lower()

if playing!="yes":
    quit()

score = 0
print("Lets gets started :) ")
answer = input("What does RAM stands for? ").lower()
if answer =="random asses memory":
    print("Correct!")
    score+=1
else:
    print("Inccorect!")

answer = input("what does CPU stands for? ").lower()
if answer =="central processing unit":
    print("Correct!")
    score+=1
else:
    print("Inccorect!")

answer = input("What does GPU stand for? ").lower()
if answer =="graphics processing unit":
    print("Correct!")
    score+=1
else:
    print("Inccorect!")

answer = input("What does PU stand for? ").lower()
if answer =="power supply":
    print("Correct!")
    score+=1
else:
    print("Inccorect!")

print("You got " + str(score) + " Correct!")
print("You got "+str((score/4)*100)+" %")