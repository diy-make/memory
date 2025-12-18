import sys
from PIL import Image

def validate_png(file_path):
    """
    Validates if a file is a valid PNG.
    """
    try:
        with Image.open(file_path) as img:
            img.verify()
        print(f"'{file_path}' is a valid PNG.")
        return True
    except (IOError, SyntaxError) as e:
        print(f"Error: '{file_path}' is not a valid PNG. Reason: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_png.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not validate_png(file_path):
        sys.exit(1)
