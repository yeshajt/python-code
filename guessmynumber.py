from random import randint
correct_answer = randint(1,101)
print "Hello, what is your name?"
name = raw_input()
print "Well, "+str(name)+", I am thinking of a number from 1 to 100."
for i in range(1, 9):
    if (i < 8):
        print "Take a guess."
        guess = raw_input()
        if (int(guess) > int(correct_answer)):
            print "Too high! Go lower."
        elif (int(guess) < int(correct_answer)):
            print "Too low! Go higher."
        else:
            print "Good job! You guessed my number in "+str(i)+" tries!"
    else:
        print "Take a guess."
        guess = raw_input()
        if (int(guess) != int(correct_answer)):
            print "Sorry, you couldn't guess my number. My number was "+str(correct_answer)+" ."
        else:
            print "Good job! You guessed my number in "+str(i)+" tries!"
