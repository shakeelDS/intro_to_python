# Create my list of numbers - here using the list function 
# and the range function - remember range is exclusive!

numbers_1_to_30 = range(1, 31)

# Create the control flow

for each_number in numbers_1_to_30:
    if (each_number % 3 == 0) & (each_number % 5 == 0) :
        print("FizzBuzz")
    elif (each_number % 3 == 0) :
         print("Fizz")
    elif (each_number % 5 == 0) :
         print("Buzz")
    else:
        print(each_number)
  

# Or you could use a while loop

#number = 1

#while number < 31:
#    if (number % 3 == 0) & (number % 5 == 0):
#        print("FizzBuzz")
#    elif (number % 3 == 0):
#        print("Fizz")
#    elif (number % 5 == 0):
#        print("Buzz")
#    else:
#        print(number)
#    number += 1          