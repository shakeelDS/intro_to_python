# Sort the titanic DataFrame by the age column

titanic_sorted = titanic.sort_values(by="age", ascending=False)
titanic_sorted.head(20)