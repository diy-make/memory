import dspy
import os
import argparse
from PIL import Image
import google.generativeai as genai

# --- DSPy Configuration ---
# Configure DSPy to use the Gemini model.
# By not providing an api_key, it should use the default authentication
# of the environment, which is the user's login.
try:
    gemini = dspy.Google(model="gemini-1.5-flash")
    dspy.settings.configure(lm=gemini)
    print("DSPy configured with Gemini successfully.")
except Exception as e:
    print(f"Error configuring DSPy with Gemini: {e}")
    exit()

# --- DSPy Signature for Image Description ---
class GenerateImageDescription(dspy.Signature):
    """Given an image, generate a one-sentence description of its content."""
    image = dspy.InputField(desc="The image to be described.")
    description = dspy.OutputField(desc="A one-sentence description of the image.")

# --- DSPy Module for Image Description ---
class ImageDescriber(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate_description = dspy.Predict(GenerateImageDescription)

    def forward(self, image_path):
        try:
            image = Image.open(image_path)
            prediction = self.generate_description(image=image)
            return prediction.description
        except Exception as e:
            print(f"Error processing image {image_path}: {e}")
            return "Could not generate a description for this image."

# --- Main Script Logic ---
def describe_images_in_folder(folder_path):
    """
    Iterates through images in a folder, generates a description for each,
    and saves the description to a markdown file.
    """
    print(f"\n--- Starting Image Description Process for: {folder_path} ---")

    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        return

    describer = ImageDescriber()

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_path = os.path.join(folder_path, filename)
            print(f"  - Processing: {filename}")

            # Generate the description
            description = describer.forward(image_path=image_path)

            # Create the markdown file
            md_filename = os.path.splitext(filename)[0] + ".md"
            md_path = os.path.join(folder_path, md_filename)

            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(f"# {filename}\n\n")
                f.write(f"![{description}]({filename})\n\n")
                f.write(f"*{description}*\n")

            print(f"    - Created description file: {md_filename}")

    print("\n--- Image Description Process Complete ---")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate descriptions for images in a folder.")
    parser.add_argument("folder_path", type=str, help="The path to the folder containing the images.")
    args = parser.parse_args()

    describe_images_in_folder(args.folder_path)
