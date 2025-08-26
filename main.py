# main.py
from helpers import sanctuaryStations, phototransQuery, seastarsQuery, createOutputJSON, writeOutputJSON

# --- Load stations ---
stationsFile = 'https://www.researchworkspace.com/files/44959120/marine_photoplot_sites_mbnms.json'
inputJSON = sanctuaryStations(stationsFile)
print('inputJSON finished reading: ',inputJSON)

# --- Ask user for input ---
sourceDataName = input("Enter source data (MARINe Transects / MARINe Photoplots / MARINe Seastars): ")
targetAssemblage = input("Enter target assemblage (e.g., Mytilus): ")
speciesName = input("Enter species name (e.g., Mytilus californianus): ")
timeFormat = "YYYY"

# --- Branching logic depending on type of MARINe dataset ---
if sourceDataName == "MARINe Transects":
    dataFile = "https://www.researchworkspace.com/file/45117911/transects_ingest_20250801.csv"
    sourceDataURL = "doi: 10.6085/AA/marine_ltm.4.14"
    variableUnit = "Percent Cover"
    variable = "organismQuantity"
    aggFunction = "mean"
    df = phototransQuery(dataFile, targetAssemblage, speciesName)

elif sourceDataName == "MARINe Photoplots":
    dataFile = "https://researchworkspace.com/files/45117169/photoplots_ingest_20250801.csv"
    sourceDataURL = "doi: 10.6085/AA/marine_ltm.4.14"
    variableUnit = "Percent Cover"
    variable = "organismQuantity"
    aggFunction = "mean"
    df = phototransQuery(dataFile, targetAssemblage, speciesName)

elif sourceDataName == "MARINe Seastars":
    dataFile = "https://www.researchworkspace.com/file/45134907/seastars_ingest_08042025.csv"
    sourceDataURL = "doi: 10.6085/AA/marine_ltm.4.13"
    variableUnit = "Total Counts"
    variable = "individualCount"
    aggFunction = "sum"
    df = seastarsQuery(dataFile, speciesName)

else:
    raise ValueError("Invalid source data name entered!")

# --- Process output ---
outputJSON, pivot_df = createOutputJSON(
                    inputJSON, df, variable, variableUnit, timeFormat, 
                    targetAssemblage, speciesName, sourceDataName, sourceDataURL, aggFunction
)
writeOutputJSON(outputJSON)


