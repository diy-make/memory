import random
import string
import sys

# --- Versioning Note ---
# This script is part of the "Salted Release Process".
# It generates a random salt to break the "Barber Paradox" by ensuring
# every release commit has a unique identifier that verify_environment.py
# can look back at in the Git history.
# -----------------------

def generate_salt_local(length=8):
    """Generates a random alphanumeric string locally."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

if __name__ == "__main__":
    # Version is passed as an argument for reporting, but doesn't affect the salt logic.
    version = sys.argv[1] if len(sys.argv) > 1 else "DEVELOPMENT"
    generated_salt = generate_salt_local()
    
    print(f"Target Version: {version}")
    print(f"Generated Salt: {generated_salt}")
