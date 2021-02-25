#Write a function that converts from Fahrenheit to degrees Celsius using the equation below.

def fahrenheit_to_degrees_celsius(degrees_f):
    degrees_c = (5 / 9) * (degrees_f - 32)
    return degrees_c

fahrenheit_to_degrees_celsius(degrees_f=81.3)