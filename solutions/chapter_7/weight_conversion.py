# Write a for loop to convert all of these measurements to kilograms (kg).
# Define my list again

grams = [100000, 7899900, 967312, 49185, 6100]

# Create the for loop

for each_weight in grams:
    kg = each_weight / 1000
    print(kg)
    
# Or we can store the values as a new list

#new_kg_list = [] # Create a blank list - this needs to be outside our loop or we'll overwrite it each time!

#for each_weight in grams:
#    kg = each_weight/1000
#    new_kg_list.append(kg)
    
#new_kg_list        