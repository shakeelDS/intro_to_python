# Using `marvel_left` and `marvel_right` perform a left join.
# Join on BOTH name and year columns.
# Note that the names of these columns may not be the same in both DataFrames.
# Use the help function to explore solutions to this. 

marvel_left_merge = marvel_left.merge(right=marvel_right , 
                                      how="left" ,
                                      left_on=["name", "year"],
                                      right_on=["name", "release_year"],
                                      indicator=True)
marvel_left_merge.head()

# Notice here we use the paramater left_on to list the names of the columns
# in our left dataframe
# and right_on for the names of the columns in our right.

# As we're using multiple columns these are in lists.