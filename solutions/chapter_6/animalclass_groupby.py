pump_hours_mean = animals.groupby(by=["Borough", "AnimalClass"])['PumpHoursTotal'].mean()

pump_hours_mean.head()