print "Enter a temperature:"
initial_temp = raw_input()
initial_temp2 = float(initial_temp)
print "Is this temperature in Fahrenheit or Celcius (F or C)?"
initial_unit = raw_input()
if (initial_unit== "F"):
    temp_converter = (5.0/9)*(float(initial_temp)-32)
    temp_rounder = round(temp_converter, 1)
    print "The temperature in Celcius is"+" "+str(temp_rounder)+" "+"degrees."
elif (initial_unit=="C"):
    temp_converter2 = (9.0/5)*float(initial_temp)+32
    temp_rounder2 = round(temp_converter2, 1)
    print "The temperature in Fahrenheit is"+" "+str(temp_rounder2)+" "+"degrees."
else:
    try:
        print "Please print F or C"
    except:
        print "Please enter a number for the temperature"
