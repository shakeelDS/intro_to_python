#Create a new boolean column in the `animals` DataFrame.
#Use the `AnimalClass` column to find the values that are eqivalant to `Fish`
#Call your new column `fish_bool`.

animals["fish_bool"] = animals["AnimalClass"] == "Fish"

# Test if it's worked with a filter
animals[animals['AnimalClass'] == "Fish"] 