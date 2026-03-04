import urllib.parse
import webbrowser
import time
import pyautogui
from DataHandler import FormatAddress

def GenerateMessageTemplate(customerName, registeredAddress):
    """
    Creates the personalized text message using placeholders for privacy.
    """
    messageText = f"""Olá {customerName}, tudo certo? Aqui é o [YOUR NAME], da [YOUR COMPANY]. ✌🏼
Estamos finalizando as últimas entregas das recompensas físicas do [PROJECT NAME]. Como tivemos alguns atrasos por questões logísticas, estamos agora enviando manualmente pelos Correios. 📦

Gostaríamos de confirmar se o endereço que temos registrado continua o mesmo:
{registeredAddress}

Se houve alguma alteração, por favor nos avise para que possamos atualizar antes da próxima remessa, para que possamos nos organizar para enviar suas recompensas físicas em breve. ✨
Agradecemos muito pela paciência e pelo apoio ao projeto, e pedimos desculpas pela demora! 💜

Grande abraço!"""
    return messageText

def SendAutomatedMessages(dataFrame):
    """
    Iterates through the DataFrame and automates the WhatsApp Web interface to send messages.
    """
    for index, rowItem in dataFrame.iterrows():
        # Extract and format the customer's first name
        fullName = str(rowItem['*Nome Destinatário'])
        customerName = fullName.split()[0] if fullName else "Apoiador"
        
        # Extract and sanitize the phone number
        rawPhoneNumber = str(rowItem['**Celular Destinatário'])
        phoneNumber = ''.join(filter(str.isdigit, rawPhoneNumber))

        # Prepare the message content
        registeredAddress = FormatAddress(rowItem)
        finalMessage = GenerateMessageTemplate(customerName, registeredAddress)

        # Encode and create the WhatsApp Web URL
        encodedMessage = urllib.parse.quote(finalMessage)
        whatsappLink = f"https://web.whatsapp.com/send?phone={phoneNumber}&text={encodedMessage}"

        # Execute the browser automation
        webbrowser.open(whatsappLink)
        
        # Wait for the page to load (adjust as necessary)
        time.sleep(15)
        
        # Send the message
        pyautogui.press('enter')
        time.sleep(3)
        
        # Close the current browser tab
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(2)