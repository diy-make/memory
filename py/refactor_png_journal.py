import os
import re
import shutil

def refactor_png_journal():
    """
    Refactors the PNG journal by moving files to dated directories and consolidating markdown files.
    """
    png_inbox = "repos/diy-make/memory/public/png/"
    public_root = "repos/diy-make/memory/public/"

    # --- 1. Get all PNG files ---
    all_files = os.listdir(png_inbox)
    png_files = [f for f in all_files if f.endswith(".png")]

    # --- 2. Process each PNG ---
    for png_filename in png_files:
        if png_filename == "01-a-screenshot-of-a-computer-screen-likely-showing-c.png":
            continue

        # --- a. Parse date ---
        date_str = None
        # Try YYYY-MM-DD format
        match = re.search(r"(\d{4}-\d{2}-\d{2})", png_filename)
        if match:
            date_str = match.group(1)
        
        # Try YYYY-Q#-MM-DD format
        if not date_str:
            match = re.search(r"(\d{4})-Q\d-(\d{2}-\d{2})", png_filename)
            if match:
                date_str = f"{match.group(1)}-{match.group(2)}"

        if not date_str:
            print(f"Could not parse date from {png_filename}, skipping.")
            continue
        
        year, month, day = date_str.split("-")
        
        # --- b. Create directories ---
        # Assuming Q4 for now, this could be improved
        day_path_png = os.path.join(public_root, year, "Q4", month, day, "png")
        day_path_md = os.path.join(public_root, year, "Q4", month, day, "md")
        os.makedirs(day_path_png, exist_ok=True)
        os.makedirs(day_path_md, exist_ok=True)

        # --- c. Determine new sequential name ---
        existing_pngs = os.listdir(day_path_png)
        new_seq_num = len(existing_pngs) + 1
        
        # --- d. Get description and key takeaway ---
        md_filename = png_filename.replace(".png", ".md")
        md_path = os.path.join(png_inbox, md_filename)
        
        title = ""
        description = ""
        key_takeaway = ""

        if os.path.exists(md_path):
            with open(md_path, 'r') as f:
                content = f.read()
                
                title_match = re.search(r"\*\*([^*]+)\*\*", content)
                if title_match:
                    title = title_match.group(1).strip()

                desc_match = re.search(r"\*([^*]+)\*", content, re.DOTALL)
                if desc_match:
                    description = desc_match.group(1).strip()

                kt_match = re.search(r"\*   \*\*Key Takeaway:\*\*([^*]+)", content)
                if kt_match:
                    key_takeaway = kt_match.group(1).strip()
        
        if not title:
            title = os.path.splitext(png_filename)[0].replace("_", " ").replace("-", " ").title()
        if not description:
            description = "No description found."
        if not key_takeaway:
            key_takeaway = "No key takeaway found."


        new_filename_base = f"{new_seq_num:02d}-{title.lower().replace(' ', '-')}"
        new_png_filename = f"{new_filename_base}.png"
        new_md_filename = f"{new_filename_base}.md"
        
        # --- e. Move and Rename PNG ---
        old_png_path = os.path.join(png_inbox, png_filename)
        new_png_path = os.path.join(day_path_png, new_png_filename)
        shutil.move(old_png_path, new_png_path)

        # --- f. Append to daily journal ---
        daily_journal_path = os.path.join(day_path_md, f"{date_str}_png_journal.md")
        
        journal_entry = f"""
---

**{new_seq_num}. {title}**
![{new_png_filename}](../../png/{new_png_filename})
*{description}*
*   **Key Takeaway:** {key_takeaway}
"""
        with open(daily_journal_path, 'a') as f:
            f.write(journal_entry)
            
        # --- g. Remove old md file ---
        if os.path.exists(md_path):
            os.remove(md_path)

if __name__ == "__main__":
    refactor_png_journal()
