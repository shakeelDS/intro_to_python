# Using `marvel_left` and `marvel_right` perform an outer join using the column `name` 

marvel_outer = marvel_left.merge(right=marvel_right, 
                                 how="outer",
                                 on="name", 
                                 indicator=True)
marvel_outer.head()