animalclass_sum = animals.groupby(by="AnimalClass")['IncidentNominalCost(£)'].sum()

animalclass_sum