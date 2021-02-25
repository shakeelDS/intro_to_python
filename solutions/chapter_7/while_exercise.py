#Code a while loop with the following characteristics:
#Assign the value of a variable temperature to be 40.
#The condition of the while loop, should check if the temperature is higher than 20
#The first command in the body should print out "Its way too hot!"
#The next command should decrease the temperature by 2 and assign this new value to temperature again.

temperature = 40

while temperature > 20:
    print("It's way too hot, it's",  temperature)
    temperature -= 2