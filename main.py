import pywhatkit as kit
import time
import pyautogui
from datetime import datetime

# Define the recipient's phone number and message
phone_numbers = ["+31 6 28401213", "+31 6 28401213"]  # Include country code, e.g., +1 for the US
message = "Vergeet niet de survey in te vullen!"

# Get the current time and calculate the time to send the message
now = datetime.now()
send_hour = 9  # 17:00 or 5:00 PM
send_minute = 56  # Set the minute for the message

for number in phone_numbers:
    kit.sendwhatmsg(number, message, send_hour, send_minute)
    send_minute += 1
    pyautogui.hotkey('ctrl', 'w')

    # with pyautogui.hold(['command']):
    #     time.sleep(1)
    #     pyautogui.press('w')