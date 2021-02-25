# Sort the titanic DataFrame by the age column

titanic_sorted = titanic.sort_values(by=["age", "sex"])
titanic_sorted.head(20)

# Check out indexes 657, 658 and 1111. 
# They are sorted first by age (0.75) and then by sex 
# with Female being first, as F is before M alphabetically.