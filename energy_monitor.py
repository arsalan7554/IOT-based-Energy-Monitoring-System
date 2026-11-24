import serial
import csv
import os
from datetime import datetime
import time

# ---- SETTINGS ----
PORT = 'COM7'        # you'll change this later when hardware arrives
BAUD = 9600
CSV_PATH = r'D:\Projects\EnergyMonitor\data\readings.csv'
# ------------------

# Create CSV file with headers if it doesn't exist
if not os.path.exists(CSV_PATH):
    with open(CSV_PATH, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'current_a', 'power_w'])

print("Connecting to Arduino...")

ser = serial.Serial(PORT, BAUD, timeout=1)
print("Connected! Reading data...")

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        if line:
            parts = line.split(',')
            if len(parts) == 3:
                current = parts[1]
                power = parts[2]
                timestamp = datetime.now().isoformat()

                # Save to CSV
                with open(CSV_PATH, 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([timestamp, current, power])

                print(f"Current: {current}A | Power: {power}W")

    except KeyboardInterrupt:
        print("Stopped.")
        break
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(1)
