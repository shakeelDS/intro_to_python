# Filter the animals DataFrame:

# Filter the animals DataFrame where the IncidentNominalCost(£) Column was less than £400 *and* where the Borough coloumn value is Croydon.


cost_u400_croydon = animals[(animals['IncidentNominalCost(£)'] < 400) & (animals['Borough'] == "Croydon")]

cost_u400_croydon.head()