import dspy
import os
import shutil
from datetime import datetime

# --- DSPy Configuration (placeholder) ---
# In a real scenario, configure your language model here.
# For example:
# turbo = dspy.OpenAI(model='gpt-3.5-turbo')
# dspy.configure(lm=turbo)

# --- DSPy Signature ---
class ScreenshotNamer(dspy.Signature):
    """Generates a descriptive filename for a screenshot based on its content."""
    image_description = dspy.InputField(desc="A description of the screenshot's content.")
    original_filename = dspy.InputField(desc="The original filename of the screenshot, which contains the timestamp.")
    
    descriptive_filename = dspy.OutputField(desc="The new, descriptive filename for the screenshot, preserving the timestamp.")

# --- DSPy Module ---
class ScreenshotNamerModule(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate_name = dspy.Predict(ScreenshotNamer)

    def forward(self, image_description, original_filename):
        return self.generate_name(image_description=image_description, original_filename=original_filename)

# --- Helper Functions ---
def get_image_description(image_path):
    """
    Placeholder function to get a description of an image.
    In a real implementation, this would use a multi-modal model to analyze the image.
    For this demo, we'll use a simplified description based on the filename.
    """
    return f"A screenshot of a computer screen, likely showing code or a terminal, taken on {image_path}"

def get_descriptive_filename(image_path, counter):
    """
    Generates a descriptive filename for a screenshot.
    """
    # In a real scenario, we would use a multi-modal model to get a description.
    # For now, we will simulate this by creating a descriptive name based on the file path.
    description = get_image_description(image_path)
    kebab_case_description = description.lower().replace(" ", "-").replace(",", "").replace(".", "")
    
    # Limit the length of the filename
    kebab_case_description = kebab_case_description[:50]
    
    return f"{counter:02d}-{kebab_case_description}.png"

# --- Main Orchestration Script ---
def orchestrate_screenshot_organization(memory_repo_root, source_png_dir):
    print("\n--- Starting DSPy Screenshot Organization ---")

    if not os.path.exists(source_png_dir) or not os.listdir(source_png_dir):
        print("No screenshots found in the source directory. Skipping.")
        return

    # Group screenshots by day
    screenshots_by_day = {}
    for filename in os.listdir(source_png_dir):
        if filename.endswith(".png"):
            # Extract date from filename (e.g., "Screenshot from 2025-12-12 08-39-41.png")
            try:
                date_str = filename.split(" ")[2]
                day = datetime.strptime(date_str, "%Y-%m-%d").day
                month = datetime.strptime(date_str, "%Y-%m-%d").month
                year = datetime.strptime(date_str, "%Y-%m-%d").year
                quarter = f"Q{(month - 1) // 3 + 1}"
                
                day_key = f"{year}/{quarter}/{month:02d}/{day:02d}"
                if day_key not in screenshots_by_day:
                    screenshots_by_day[day_key] = []
                screenshots_by_day[day_key].append(filename)
            except (IndexError, ValueError):
                print(f"Could not parse date from filename: {filename}. Skipping.")

    for day_path, filenames in screenshots_by_day.items():
        print(f"\nProcessing screenshots for day: {day_path}")

        # Define paths
        day_png_dir = os.path.join(memory_repo_root, day_path, "png")
        day_md_dir = os.path.join(memory_repo_root, day_path, "md")
        os.makedirs(day_png_dir, exist_ok=True)
        os.makedirs(day_md_dir, exist_ok=True)

        renamed_files = []
        counter = 1

        for original_filename in filenames:
            original_path = os.path.join(source_png_dir, original_filename)
            
            # 1. Get descriptive filename
            new_filename = get_descriptive_filename(original_path, counter)
            counter += 1

            new_path = os.path.join(day_png_dir, new_filename)

            # 2. Rename and move the file
            shutil.move(original_path, new_path)
            print(f"Moved and renamed: {original_filename} -> {new_filename}")
            renamed_files.append((new_filename, get_image_description(original_path)))

        # 3. Create an index.md in the png directory
        index_md_path = os.path.join(day_png_dir, "index.md")
        with open(index_md_path, 'w', encoding='utf-8') as f:
            f.write(f"# PNG Index for {day_path}\n\n")
            f.write("This file indexes all PNG images for this day.\n\n")
            for i, (filename, desc) in enumerate(renamed_files, 1):
                f.write(f"{i}. **[{filename}](./{filename})**\n")
                f.write(f"    * *Description:* {desc}\n\n")
        print(f"Created index.md for {day_path}")

        # 4. Create a Screenshots.md in the md directory
        screenshots_md_path = os.path.join(day_md_dir, "Screenshots.md")
        with open(screenshots_md_path, 'w', encoding='utf-8') as f:
            f.write(f"# Day {day_path.split('/')[-1]} Snapshots\n\n")
            for i, (filename, desc) in enumerate(renamed_files, 1):
                f.write(f"---\n\n")
                f.write(f"**{i}. {filename.replace('.png', '').replace('-', ' ').title()}**\n")
                f.write(f"![{desc}](../../png/{filename})\n")
                f.write(f"*A screenshot showing {desc.lower()}.*\n\n")
                f.write(f"*   **Key Takeaway:** \n\n")
        print(f"Created Screenshots.md for {day_path}")

    print("\n--- DSPy Screenshot Organization Complete ---")


if __name__ == "__main__":
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    memory_repo_root = os.path.dirname(current_script_dir)
    source_png_dir = os.path.join(memory_repo_root, "png")
    
    orchestrate_screenshot_organization(memory_repo_root, source_png_dir)