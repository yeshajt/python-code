import random
print "===Welcome to the States Capitals Quiz==="
states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 
         'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 
         'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 
         'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 
         'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 
         'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 
         'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 
         'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 
         'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 
         'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
capitals = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento",
           "Denver", "Hartford", "Dover", "Tallahassee", "Atlanta", "Honolulu",
           "Boise", "Springfield", "Indianapolis", "Des Moines", "Topeka",
           "Frankfort", "Baton Rouge", "Augusta", "Annapolis", "Boston",
           "Lansing", "St. Paul", "Jackson", "Jefferson City", "Helena",
           "Lincoln", "Carson City", "Concord", "Trenton", "Santa Fe",
           "Albany", "Raleigh", "Bismarck", "Columbus", "Oklahoma City",
           "Salem", "Harrisburg", "Providence", "Columbia", "Pierre",
           "Nashville", "Austin", "Salt Lake City", "Montpelier", "Richmond",
           "Olympia", "Charleston", "Madison", "Cheyenne"]
correct = 0
correct_states = []
incorrect = 0
incorrect_states = []
incorrect_capitals = []
#picks 10 random states
for i in range(1,len(states)):
    random_state = int((len(states)-1)*(random.random()))
    state1 = states[random_state]
    print "What is the capital of " + str(state1) + "?"
    capital1 = raw_input()
    correct_capital = capitals[random_state]
    #determines whether the answer is correct or not
    if (capital1 == correct_capital):
        print "Correct."
        correct = correct + 1
        correct_states.append(state1)
    else:
        try:
            #user error
            correct_letter = 0
            incorrect_letter = 0
            #capitalization check
            if (capital1.title() == correct_capital):
                print "Correct, but you need to capitalize the first letter."
            #spelling errors
            else:
                for i in range(0, len(capital1)):
                    if (capital1[i] == correct_capital[i]):
                        correct_letter = correct_letter + 1
                        correct_states.append(state1)
                    else:
                        incorrect_letter = incorrect_letter + 1
                if (len(correct_capital)-correct_letter == 1) or (len(correct_capital)-correct_letter == 2):
                    print "Correct, but you have a spelling error."
                    correct = correct + 1
                    correct_states.append(state1)
                else:
                    print "Incorrect."
                    incorrect = incorrect + 1 
                    incorrect_states.append(state1)
                    incorrect_capitals.append(correct_capital)
        except:
            print "Incorrect."
            incorrect = incorrect + 1
            incorrect_states.append(state1)
            incorrect_capitals.append(correct_capital)
    states.remove(state1)
    capitals.remove(correct_capital)
#determines the final score
final_score = int((float(correct)/50.0)*100)
print "You scored " + str(final_score) + "% on the test."
if (final_score == 100):
    print "Good job!"
else:
    print "These are the correct countries and capitals:"
    for i in range(0, len(incorrect_states)):
        print incorrect_states[i], incorrect_capitals[i]
    print "Better luck next time!"

