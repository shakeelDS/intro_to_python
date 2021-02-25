# Filter the titanic DataFrame by age column; return the values over 40.

titanic_over40 = titanic[titanic['age'] > 40]
titanic_over40.head()