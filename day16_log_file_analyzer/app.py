print("🧾 Log File Analyzer")

error_count = 0
warning_count = 0
info_count = 0

with open("app.log", "r") as file:
    for line in file:
        line = line.upper()

        if "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "INFO" in line:
            info_count += 1

print("\n📊 Log Analysis Result:")
print(f"ERRORS   : {error_count}")
print(f"WARNINGS : {warning_count}")
print(f"INFO     : {info_count}")