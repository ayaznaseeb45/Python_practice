from datetime import datetime
file = open("activity_log.txt", "w")
content = file.write(f"{datetime.now}")
print("Activity logged successfully.")


with open ("activity_log.txt", "r") as file:
    for line in file:
        print(line.strip)

try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: File not found!")


import logging
from datetime import datetime

logging.basicConfig(filename="app.log", level=logging.INFO)

try:
    with open("data.txt", "r") as f:
        content = f.read()
        logging.info(f"File opened successfully at {datetime.now()}")
except FileNotFoundError:
    logging.error(f"File not found at {datetime.now()}")

