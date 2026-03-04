import os
from DataHandler import LoadCustomerData, LoadMessageTemplate
from MessageSender import SendAutomatedMessages

def RunApplication():
    """
    Main function to initialize the application, load external files, and trigger automation.
    """
    # Define paths based on the script location
    scriptDirectory = os.path.dirname(os.path.abspath(__file__))
    csvFilePath = os.path.join(scriptDirectory, "..", "data", "contacts.csv")
    templateFilePath = os.path.join(scriptDirectory, "..", "data", "message_template.txt")
    
    try:
        # Load external configurations
        print("Loading data files...")
        customerData = LoadCustomerData(csvFilePath)
        baseTemplate = LoadMessageTemplate(templateFilePath)
        
        # Execute the workflow
        print("Starting WhatsApp automation. Please do not use your mouse or keyboard...")
        SendAutomatedMessages(customerData, baseTemplate)
        
        print("Automation finished successfully.")
        
    except FileNotFoundError as fileError:
        print(f"Configuration error: {fileError}. Make sure the files exist in the 'data' folder.")
    except Exception as applicationError:
        print(f"An unexpected error occurred: {applicationError}")

if __name__ == "__main__":
    RunApplication()