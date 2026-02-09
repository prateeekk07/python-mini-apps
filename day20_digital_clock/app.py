import time
from datetime import datetime

print("⏰ Digital Clock - Day 20")
print("Press Ctrl + C to stop\n")

try:
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"\rCurrent Time: {current_time}", end="")
        time.sleep(1)

except KeyboardInterrupt:
    print("\n\n👋 Clock stopped. Bye!")