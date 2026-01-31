from datetime import datetime
from zoneinfo import ZoneInfo   # Python 3.9+

print("🌍 World Clock")

print("Choose a country:")
print("1. India")
print("2. USA (New York)")
print("3. UK (London)")
print("4. Japan")

choice = input("Enter choice (1/2/3/4): ")

if choice == "1":
    tz = ZoneInfo("Asia/Kolkata")
    country = "India"
elif choice == "2":
    tz = ZoneInfo("America/New_York")
    country = "USA (New York)"
elif choice == "3":
    tz = ZoneInfo("Europe/London")
    country = "UK (London)"
elif choice == "4":
    tz = ZoneInfo("Asia/Tokyo")
    country = "Japan"
else:
    print("❌ Invalid choice")
    exit()

current_time = datetime.now(tz).strftime("%d-%m-%Y %H:%M:%S")

print(f"\n⏰ Current time in {country}:")
print(current_time)