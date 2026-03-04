import pandas as pd

def FormatAddress(rowItem):
    """
    Extracts and formats the address from a single CSV row into a complete string.
    """
    streetName = str(rowItem['*Logradouro Destinatário'])
    houseNumber = str(rowItem['*Número Destinatário'])
    complementText = str(rowItem['Complemento Destinatário'])
    neighborhoodName = str(rowItem['*Bairro Destinatário'])
    cityName = str(rowItem['*Cidade Destinatário'])
    stateName = str(rowItem['*UF Destinatário'])
    zipCode = str(rowItem['*CEP Destinatário'])

    fullAddress = f"{streetName}, {houseNumber}"
    
    # Check if the complement exists and is valid
    if pd.notna(rowItem['Complemento Destinatário']) and complementText.strip() != "" and complementText.lower() != "nan":
        fullAddress += f", {complementText}"
        
    fullAddress += f" - {neighborhoodName}, {cityName} - {stateName}, CEP: {zipCode}"

    return fullAddress

def LoadCustomerData(csvFilePath):
    """
    Loads the CSV file into a pandas DataFrame.
    """
    dataFrame = pd.read_csv(csvFilePath)
    return dataFrame