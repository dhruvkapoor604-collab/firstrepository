import psutil
import time

THRESHOLD = 80  # CPU usage threshold

print("Monitoring CPU usage...")

try:
    while True:
        # Get CPU usage percentage
        cpu_usage = psutil.cpu_percent(interval=1)

        # Check if CPU usage exceeds threshold
        if cpu_usage > THRESHOLD:
            print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")

except Exception as e:
    print(f"An error occurred: {e}")
