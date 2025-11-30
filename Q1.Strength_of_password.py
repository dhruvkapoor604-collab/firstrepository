import re
# Function to check password strength
def check_password_strength(password):
    # Minimum length check
    if len(password) < 8:
        return False
    
    # Uppercase letter check
    if not re.search(r"[A-Z]", password):
        return False
    
    # Lowercase letter check
    if not re.search(r"[a-z]", password):
        return False
    
    # Digit check
    if not re.search(r"[0-9]", password):
        return False
    
    # Special character check
    if not re.search(r"[!@#$%]", password):
        return False
    
    # If all conditions passed
    return True
# Main script asking user for input
user_password = input("Enter a password to check its strength: ")
if check_password_strength(user_password):
    print("Password is STRONG ✔")
else:
    print("Password is WEAK ✘ — Please include uppercase, lowercase, digit, and special characters.")
