# Update the function to round to 1 decimal place


def rnd_fahrenheit_to_degrees_celsius(degrees_f):
    degrees_c = (5 / 9) * (degrees_f - 32)
    return round(degrees_c, 1)  

rnd_fahrenheit_to_degrees_celsius(81.3)

# Note the round() function has to be in the return statement.
# I can also save the output of round() to a variable like so:



# def rnd1_fahrenheit_to_degrees_celsius(degrees_f):
#    degrees_c = (5/9) * (degrees_f- 32)
#    rounded_c = round(degrees_c, 1 )  
#    return rounded_c

# Note the round() function has to be in the return statement.

#rnd1_fahrenheit_to_degrees_celsius(81.3)
