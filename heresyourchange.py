n = 0
while (n == 0):
    try:
        print "What is the cost?"
        original_cost = raw_input()
        original_cost = float(original_cost)
        print "How much did you pay?"
        amount_paid = raw_input()
        amount_paid = float(amount_paid)
        change = amount_paid - original_cost
        #error checking
        if (change < 0):
            print "The amount you paid is too low."
        elif (change > 10):
            print "The amount you paid is too high."
        else:
            print "Here's your change: "
            #calculates the change in dollars
            dollars = int(change/1)
            amount_left = change % 1
            final_dollars = dollars
            if (final_dollars == 1):
                print str(final_dollars) + " dollar."
            else:
                print str(final_dollars) + " dollars."
            #calculates the change in quarters
            quarters = int(amount_left/0.25)
            amount_left_quarters = amount_left % 0.25
            #rounded amount left due to binary glitches in python
            rounded_amount_left = round(amount_left_quarters, 2)
            final_quarters = quarters
            if (final_quarters == 1):
                print str(final_quarters) + " quarter."
            else:
                print str(final_quarters) + " quarters."
            #calculates the change in dimes
            dimes = int(rounded_amount_left/0.1)
            amount_left_dimes = rounded_amount_left % 0.1
            final_dimes = dimes
            if (final_dimes == 1):
                print str(final_dimes) + " dime."
            else:
                print str(final_dimes) + " dimes."
            #calculates the change in nickels
            nickels = int(amount_left_dimes/0.05)
            amount_left_nickels = amount_left_dimes % 0.05
            final_nickels = nickels
            if (final_nickels == 1):
                print str(final_nickels) + " nickel."
            else:
                print str(final_nickels) + " nickels."
            #calculates the change in pennies
            pennies = int(amount_left_nickels/0.01)
            final_pennies = pennies
            if (final_pennies == 1):
                print str(final_pennies) + " penny."
            else:
                print str(final_pennies) + " pennies."
            n = 1
    except:
        print "Please provide a number"
