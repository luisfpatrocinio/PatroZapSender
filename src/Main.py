import os
from DataHandler import LoadCustomerData
from MessageSender import SendAutomatedMessages

def RunApplication():
    """
    Main function to initialize the application and trigger the automation process.
    """
    # Define the relative path to the CSV data file
    scriptDirectory = os.path.dirname(os.path.abspath(__file__))
    csvFilePath = os.path.join(scriptDirectory, "..", "data", "sample_data.csv")
    
    # Execute the workflow
    try:
        customerData = LoadCustomerData(csvFilePath)
        SendAutomatedMessages(customerData)
        print("Automation finished successfully.")
    except FileNotFoundError:
        print(f"Error: The file {csvFilePath} was not found.")
    except Exception as applicationError:
        print(f"An unexpected error occurred: {applicationError}")

if __name__ == "__main__":
    RunApplication()