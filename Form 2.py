import datetime
import webbrowser
import urllib.parse

def material_request(datetime_val, employee_name, date_of_clip, time_of_clip, purpose, client_name, received_by):
    # Create the structured dictionary
    request = {
        "Request Date": datetime_val.strftime("%Y-%m-%d %H:%M"),
        "Employee": employee_name,
        "Clip Date": date_of_clip,
        "Clip Time": time_of_clip,
        "Purpose": purpose,
        "Client": client_name,
        "Received By": received_by
    }
    return request

print("--- Tech Hub Solutions: Material Request Form ---")

prompt = input("Are you requesting recorded material? (yes/no): ").strip().lower()
if prompt != 'yes':
    print("No material request made.")
    exit()

# Data Collection
employee_name = input("Enter Employee Name: ")
purpose = input("Enter Purpose of Request: ")
client_name = input("Enter Client Name: ")
date_of_clip = input("Enter Date of Clip: ")
time_of_clip = input("Enter Time of Clip: ")
received_by = input("Enter Name of Receiver: ")

request_data = material_request(datetime.datetime.now(), employee_name, date_of_clip, time_of_clip, purpose, client_name, received_by)

# --- NEW: WhatsApp Integration Logic ---

# 1. Format the message for WhatsApp
message = "*NEW MATERIAL REQUEST*\n\n"
for key, value in request_data.items():
    message += f"*{key}:* {value}\n"

# 2. Set the recipient phone number (Include country code, no + or spaces)
# Example: 1234567890
phone_number = "+263773021796" 

# 3. Encode the message for a URL and open the browser
encoded_message = urllib.parse.quote(message)
whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_message}"

print("\nOpening WhatsApp to send request...")
webbrowser.open(whatsapp_url)

print("Request details prepared successfully.")