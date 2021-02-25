# Change the weight_kg column to a int datatype.

# 1 - Identify

print(pun_animals[~pun_animals["weight_kg"].str.isdigit()])

# Filtering pun animals for the inverse (~) of the .isdigit() will return the one that is not a digit 

# 2 - Fix  Change the "113kg" value to 113

pun_animals.loc[pun_animals["weight_kg"] == "113kg", "weight_kg"] = 113

# Using .str.replace() will also work

# pun_animals['weight_kg'] = pun_animals['weight_kg'].str.replace("113kg", "113")

# Just replacing the letters kg with nothing (an empty string) makes it more generalisable!

# # pun_animals['weight_kg'] = pun_animals['weight_kg'].str.replace("kg", "")

# 3 - Convert the type

pun_animals["weight_kg"] = pun_animals["weight_kg"].astype("float64")

# print out changed column dtypes

print(pun_animals["weight_kg"].dtypes)
