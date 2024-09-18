import pywhatkit as kit
import time
import pyautogui
from datetime import datetime

# Define the phone numbers and the message
phone_numbers = ["+31 6 12345678"]  # Include country code, e.g., +31 6 12345678
message = "Dit is een automatisch gegenereerd bericht: vergeet a.u.b. niet de survey in te vullen vanavond!"

# Get the current time and calculate the time to send the message
now = datetime.now()
send_hour = 9  # for example: 9 AM = 9 and 5 PM = 17
send_minute = 5  # Set the minute for the message, never add a 0 before the number

# Send the message
for number in phone_numbers:
    kit.sendwhatmsg(number, message, send_hour, send_minute)
    time.sleep(15) # Recovery time has to be 15 seconds
    send_minute += 1 # Next message needs to be sent a minute after start time
    pyautogui.hotkey('ctrl', 'w') # Close window
