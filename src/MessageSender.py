import urllib.parse
import webbrowser
import time
import pyautogui
from DataHandler import FormatAddress

def GenerateMessageTemplate(baseTemplate, customerName, registeredAddress):
    """
    Replaces the placeholders in the base template with actual customer data.
    """
    finalMessage = baseTemplate.replace("{Nome}", customerName)
    finalMessage = finalMessage.replace("{Endereco}", registeredAddress)
    
    return finalMessage

def SendAutomatedMessages(dataFrame, baseTemplate):
    """
    Iterates through the DataFrame and automates the WhatsApp Web interface.
    """
    for index, rowItem in dataFrame.iterrows():
        # Extract and format the customer's first name
        fullName = str(rowItem['*Nome Destinatário'])
        customerName = fullName.split()[0] if fullName else "Apoiador"
        
        # Extract and sanitize the phone number
        rawPhoneNumber = str(rowItem['**Celular Destinatário'])
        phoneNumber = ''.join(filter(str.isdigit, rawPhoneNumber))

        # Check if the number length is 10 or 11 (missing country code)
        # This prevents bugs with DDD 55 (Rio Grande do Sul)
        if len(phoneNumber) == 10 or len(phoneNumber) == 11:
            phoneNumber = f"55{phoneNumber}"

        # Prepare the message content dynamically
        registeredAddress = FormatAddress(rowItem)
        finalMessage = GenerateMessageTemplate(baseTemplate, customerName, registeredAddress)

        # Encode and create the WhatsApp Web URL
        encodedMessage = urllib.parse.quote(finalMessage)
        whatsappLink = f"https://web.whatsapp.com/send?phone={phoneNumber}&text={encodedMessage}"

        # Execute the browser automation
        webbrowser.open(whatsappLink)
        
        # Wait for the page to load
        time.sleep(15)
        
        # Send the message
        pyautogui.press('enter')
        time.sleep(3)
        
        # Close the current browser tab
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(2)