# Load in the police data

police = pd.read_excel("../data/police_data.xlsx", sheetname=1)

police.head()

# The paramater sheetname = 1 imports the second sheet
# sheetname = "Table P1" will also work
# Note from Pandas 0.21.0 use sheet_name = 
