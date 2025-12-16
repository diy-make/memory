import dspy
import os
import shutil
from datetime import datetime
import re
import argparse
import json

# Since we can't call a real multi-modal model, we will simulate its output.
# This dictionary maps known screenshot filenames to their analysis.
SIMULATED_ANALYSIS = {
    "Screenshot from 2025-12-14 10-00-08.png": {
        "descriptive_title": "Agent Acknowledges V1 Plan",
        "alt_text": "A screenshot showing the agent Zion acknowledging the V1 cleanup plan.",
        "description": "This screenshot shows the agent Zion acknowledging the V1 cleanup plan.",
        "key_takeaway": "The agent confirms its understanding before executing a complex, multi-step task."
    },
    "Screenshot from 2025-12-14 10-44-05.png": {
        "descriptive_title": "Agent Revises README for AL",
        "alt_text": "A screenshot showing the agent rewriting the main README.md to include the 'Artificial Life' concept.",
        "description": "A screenshot showing the agent rewriting the main README.md to include the 'Artificial Life' concept.",
        "key_takeaway": "The project's core documentation is updated to reflect its ultimate goal of creating Artificial Life."
    }
    # Add other known screenshots here...
}


class GenerateImageTitle(dspy.Signature):
    """Generate a short, descriptive, file-safe title for a screenshot from its original filename."""
    image_context = dspy.InputField(desc="The context or content of the screenshot.")
    descriptive_title = dspy.OutputField(desc="A short, human-readable, file-safe title. Example: 'User-Fixes-Git-Ignore'")

class AnalyzeImageContext(dspy.Signature):
    """Given a title, generate a detailed description and a key takeaway for the screenshot."""
    image_title = dspy.InputField(desc="The descriptive title of the screenshot.")
    alt_text = dspy.OutputField(desc="A one-sentence description of the image's content for alt-text.")
    description = dspy.OutputField(desc="A one-sentence description of the image's content for the body of the markdown file.")
    key_takeaway = dspy.OutputField(desc="A single, concise insight or conclusion drawn from the screenshot.")


class ScreenshotAnalysisModule(dspy.Module):
    def __init__(self):
        super().__init__()
        # In a real scenario, these would be dspy.Predict or dspy.ChainOfThought calls
        # self.generate_title = dspy.Predict(GenerateImageTitle)
        # self.analyze_context = dspy.Predict(AnalyzeImageContext)

    def forward(self, original_filename):
        # This is a simulated multi-modal analysis.
        # In a real scenario, this would involve a multi-modal model to analyze the image.
        # For now, we use a dictionary to simulate the analysis based on the filename.
        if original_filename in SIMULATED_ANALYSIS:
            return dspy.Example(**SIMULATED_ANALYSIS[original_filename])
        
        # Fallback for unknown images
        print(f"Warning: No simulated analysis found for {original_filename}. Using fallback.")
        fallback_title = os.path.splitext(original_filename)[0].replace(" ", "-").replace(":", "-")
        return dspy.Example(
            descriptive_title=fallback_title,
            alt_text=f"A screenshot from the session on {original_filename.split(' ')[2]}.",
            description="This screenshot has not been analyzed. A human should add a description.",
            key_takeaway="This screenshot's content has not been analyzed."
        )

def slugify(text):
    """Converts a title to a file-safe slug."""
    text = text.lower().replace(" ", "-")
    return re.sub(r'[^a-zA-Z0-9-]', '', text)

def orchestrate_screenshot_organization(memory_repo_root, source_png_dir):
    print("\n--- Starting Screenshot Organization (V3) ---")

    if not os.path.exists(source_png_dir) or not os.listdir(source_png_dir):
        print("No screenshots found in the source directory to process.")
        return

    analyzer = ScreenshotAnalysisModule()
    
    # Group screenshots by the day they were created
    screenshots_by_day = {}
    for filename in os.listdir(source_png_dir):
        if filename.endswith(".png"):
            try:
                # Assumes "Screenshot from YYYY-MM-DD HH-MM-SS.png" format
                date_str = filename.split(" ")[2]
                date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                day_key = date_obj.strftime("%Y-%m-%d")
                if day_key not in screenshots_by_day:
                    screenshots_by_day[day_key] = []
                screenshots_by_day[day_key].append(filename)
            except (IndexError, ValueError):
                print(f"Could not parse date from filename: {filename}. Skipping.")

    for day_str, filenames in screenshots_by_day.items():
        date_obj = datetime.strptime(day_str, "%Y-%m-%d")
        day_path_segment = f"{date_obj.year}/Q{(date_obj.month - 1) // 3 + 1}/{date_obj.month:02d}/{date_obj.day:02d}"
        print(f"\nProcessing {len(filenames)} screenshots for day: {day_str}")

        day_png_dir = os.path.join(memory_repo_root, day_path_segment, "png")
        day_md_dir = os.path.join(memory_repo_root, day_path_segment, "md")
        os.makedirs(day_png_dir, exist_ok=True)
        os.makedirs(day_md_dir, exist_ok=True)

        # Path for the final markdown report for this day
        report_filename = "Screenshots.md"
        report_path = os.path.join(day_md_dir, report_filename)

        # Write header to the new report file
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# Day {date_obj.day} Snapshots\n\n")

        processed_files = []
        for i, original_filename in enumerate(sorted(filenames), 1):
            original_path = os.path.join(source_png_dir, original_filename)
            
            # 1. Analyze image to get metadata
            analysis = analyzer(original_filename=original_filename)
            
            # 2. Generate new filename
            new_filename = f"{i:02d}-{slugify(analysis.descriptive_title)}.png"
            new_path = os.path.join(day_png_dir, new_filename)

            # 3. Move and rename the file
            if os.path.exists(original_path):
                shutil.move(original_path, new_path)
                print(f"  - Moved and renamed: {original_filename} -> {new_filename}")
            else:
                print(f"  - Source file not found, assuming already moved: {original_filename}")


            # 4. Append to the markdown report
            with open(report_path, 'a', encoding='utf-8') as f:
                f.write("---\n\n")
                f.write(f"**{i}. {analysis.descriptive_title}**\n")
                f.write(f"![{analysis.alt_text}]({os.path.join('../../png', new_filename)})")
                f.write(f"*{analysis.description}*\n\n")
                f.write(f"*   **Key Takeaway:** {analysis.key_takeaway}\n\n")
            
            processed_files.append(new_filename)

        # 5. Create an index.md in the daily png directory
        index_md_path = os.path.join(day_png_dir, "index.md")
        with open(index_md_path, 'w', encoding='utf-8') as f:
            f.write(f"# PNG Index for {day_str}\n\n")
            for filename in processed_files:
                f.write(f"- [{filename}]({os.path.join('../png', filename)})\n")
        print(f"Created index file at {index_md_path}")
        print(f"Appended {len(processed_files)} entries to {report_path}")

    print("\n--- Screenshot Organization Complete ---")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize screenshots into a date-based hierarchy.")
    parser.add_argument("source_dir", type=str, help="The source directory containing the screenshots.")
    parser.add_argument("--memory_repo_root", type=str, default="repos/diy-make/memory/public", help="The root of the memory repository.")
    args = parser.parse_args()

    orchestrate_screenshot_organization(args.memory_repo_root, args.source_dir)