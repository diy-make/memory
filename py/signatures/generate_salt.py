import random
import string

# --- Versioning Note ---
# This script is part of the "Salted Release Process" for the Memory Module.
# When releasing a new version (e.g., V0.9.0), this generator must be used 
# to create a unique cryptographic salt.
# This salt is then appended to the version string in `py/verify_environment.py`.
# -----------------------

def generate_salt_local(length=8):
    """Generates a random alphanumeric string locally."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

if __name__ == "__main__":
    version = "V0.9.0"
    generated_salt = generate_salt_local()
    
    print(f"Version: {version}")
    print(f"Generated Salt: {generated_salt}")