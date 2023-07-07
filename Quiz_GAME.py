print('Welcome to THE QUIZ')

playing = input("Do you want to play?\n")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play! :)")

score = 0 

answer = input ("What does the CPU stand for? ")
if answer.lower() == "control processing unit":
    print('correct!')
    score += 1

else:
    print("Wrong")
answer = input ("What does the GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('correct!') 
    score += 1

else:
    print("Wrong")

answer = input ("What does the TPU stand for? ")
if answer.lower() == "tensor processing unit":
    print('correct!')
    
    score += 1

else:
    print("Wrong")

answer = input ("What does the RAM stand for? ")
if answer.lower() == "random ccess memory ":
    print('correct!')
    score += 1

else:
    print("Wrong")

print("You got " + str(score) + " questions correct")

