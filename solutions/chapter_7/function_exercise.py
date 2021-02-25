def fizz_buzz(my_iterable):
    
    """
    fizz_buzz takes an iterable and:
    
    if numbers are divisible by 3 and 5 and returns the value of "FizzBuzz"
    
    if numbers are divisible by 3 return "Fizz"

    if numbers are divisible by 5 return "Fizz"

    else print out the number
    
    
    """
    for each_number in my_iterable:
        if (each_number % 3 == 0) & (each_number % 5 == 0) :
            print("FizzBuzz")
        elif (each_number % 3) == 0 :
            print("Fizz")
        elif (each_number % 5) == 0 :
            print("Buzz")
        else:
            print(each_number)
            
            

# Run the function - I'm passing a iterable using the range() function
# which remember is exclusive

fizz_buzz(range(1, 31))

##### Or using a while loop ####

#def fizzbuzz_while(max_number):

#    max_number +=1 # As the last number is exclusive, we can add 1 here
#    number = 1

#    while number < max_number:
#        if (number % 3 == 0) & (number % 5 == 0):
#            print("FizzBuzz")
#        elif (number % 3 == 0):
#            print("Fizz")
#        elif (number % 5 == 0):
#            print("Buzz")
#        else:
#            print(number)
#        number += 1