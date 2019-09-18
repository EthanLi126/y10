youguess = False
numtries = 0
while youguess == False:
    numtries = numtries + 1 
    correct = 974 
    print("Guess a number between 1-100") 
    guess = input("Example: 200: ")
    numguess = int(guess) 
    if (numguess == correct): 
        str_tries =  str(numtries) 
        print("Well done!")
        print("You have solved the problem in " + str_tries + " tries.") 
        youguess = True 
    else:
        if (numguess > correct): 
            print("Wrong! Too high.")
        else:
            print("Wrong! Too low.")
