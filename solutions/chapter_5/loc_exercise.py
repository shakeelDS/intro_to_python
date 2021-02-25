# Use `.loc[]` to change the value `Lamb` to `Sheep`

animals.loc[animals['AnimalGroupParent'] == "Lamb", "AnimalGroupParent"]  = "Sheep"

# Filter to show the head of my new DataFrame 
animals[animals['AnimalGroupParent'] == "Sheep"].head()
