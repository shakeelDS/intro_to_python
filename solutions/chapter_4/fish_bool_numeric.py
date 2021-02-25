# Convert fish_bool to be a numerical value.

animals["fish_bool"] = animals["fish_bool"].astype("int64")

# Check with a filter

animals[animals["AnimalClass"] == "Fish"]