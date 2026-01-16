#Recorded material request
import datetime
def material_request(datetime, employee_name,date_of_clip, time_of_clip, purpose, client_name, received_by
):
    request = {
        "datetime": datetime,
        "employee_name": employee_name,
        "date_of_clip": date_of_clip,
        "time_of_clip": time_of_clip,
        "purpose": purpose,
        "client_name": client_name,
        "received_by": received_by
    }
    return request

print("Material Request Form")

prompt = input ("Are you requesting recorded material? yes/no):").strip().lower()
if prompt != 'yes':
    print("No material request made.")
    exit()

datetime_now = datetime.datetime.now()
employee_name = input("Enter Employee Name: ")
date_of_clip = input("Enter Date of Clip (YYYY-MM-DD): ")
time_of_clip = input("Enter Time of Clip (HH:MM): ")
purpose = input("Enter Purpose of Request: ")   
client_name = input("Enter Client Name: ")
received_by = input("Enter Name of Person Receiving the Material: ")
request = material_request(datetime_now, employee_name, date_of_clip, time_of_clip, purpose, client_name, received_by)
print("Material Request Submitted:")

for key, value in request.items():
    print(f"{key}: {value}")