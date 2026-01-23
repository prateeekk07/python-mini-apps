print("📧 Email Slicer")

email = input("Enter your email address: ").strip()

if "@" in email:
    username, domain = email.split("@")
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("❌ Invalid email address")