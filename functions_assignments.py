#===functions: vowelcount.py===
from time import sleep
print "Print your word, and I will tell you how many vowels it has:"
def vowelcount(x):
    vowel_counter = 0
    x = x.lower()
    for i in x:
        if (i == "a") or (i == "e") or (i == "i") or (i == "o") or (i == "u"):
            vowel_counter += 1
    if (vowel_counter == 1):
        print "There is " + str(vowel_counter) + " vowel in this word."
    else:
        print "There are " + str(vowel_counter) + " vowels in this word."

#===functions: alpha.py===
def alpha(x):
    x = x.lower()
    x = list(x)
    if (x == sorted(x)):
        print "This word is in alphabetical order :)"
    else:
        print "This word is not in alphabetical order."
n = 0
while (n == 0):
    word = raw_input()
    try:
        vowelcount(word)
        print 
        print "Now I will tell you if your word is in alphabetical order: "
        sleep(2)
        alpha(word)
        n = 1
    except:
        print "Please print a word \r"
        sleep(2)

#===functions: prime.py===
print 
print "Print a number, and I will tell you if it's prime:"
def prime(x):
    divisible = 0
    not_divisible = 0
    for i in range(2, x-1):
        if (x % i == 0):
            divisible += 1
        else:
            not_divisible += 1
    if (divisible == 0):
        print "This is a prime number."
    else:
        print "This is not a prime number."
n = 0
while (n == 0):
    number = input()
    try:
        prime(number)
        n = 1
    except:
        print "Please print a number."


#===functions: factsum_perfect.py===
sleep(2)
def factsum(x):
    factors = 0
    for i in range(1, x-1):
        if (x % i == 0):
            factors += i
        else:
            continue
    return factors

perfect_numbers = []
def perfect():
    for i in range(1,10000):
        if (i == factsum(i)):
            perfect_numbers.append(i)
            continue
        else:
            continue
    return perfect_numbers

mersenne_numbers = []
def mersenneperfect():
    primelist = [11,13,17,19,23,29]
    for i in primelist:
        perfect_number = (2**(i-1))*((2**i)-1)
        mersenne_numbers.append(perfect_number)
    return mersenne_numbers

print 
print "These are the perfect numbers: "
perfect()
mersenneperfect()
print perfect_numbers + mersenne_numbers
