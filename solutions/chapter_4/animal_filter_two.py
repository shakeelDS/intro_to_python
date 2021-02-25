# Filter the animals DataFrame:

# Filter the animals DataFrame where the 'PropertyType' was "River/canal" or the `"PumpHoursTotal"` was greater than 8.


river_pumphours = animals[(animals['PropertyType'] == "River/canal") | (animals['PumpHoursTotal'] > 8)]

river_pumphours