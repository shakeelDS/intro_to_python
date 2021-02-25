# Filter the `titanic` DataFrame by `sex` column; return the “female” values.

titanic_female = titanic[titanic['sex'] ==  "female"]
titanic_female.head()