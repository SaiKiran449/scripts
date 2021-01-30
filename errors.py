import json
import csv

messages_file = open('messages.json',)
error_messages = json.load(messages_file)

errors_list = []

for error in error_messages:
    if error.startswith("error"):
        errors_list.append(
            {
                "Error message":error_messages.get(error).get("translations").get("en"),
                "Error Package":error.replace("error:",''),
                "File":error_messages.get(error).get("description").get("file")
            }
        )


csv_columns = ['Error message','Error Package','File']

with open('dict.csv', 'w' ) as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
    writer.writeheader()
    for error in errors_list:
            writer.writerow(error)
