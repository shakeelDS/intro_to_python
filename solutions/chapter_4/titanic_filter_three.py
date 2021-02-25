# Filter the `titanic` DataFrame by `fare` column; return the values equivalent to or less than 30.50

titanic_fare_under30 = titanic[titanic['fare'] <= 30.50]
titanic_fare_under30.head()