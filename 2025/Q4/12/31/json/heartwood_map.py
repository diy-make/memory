import json
import sys
import os
from datetime import datetime

def print_banner():
    banner = """
    🌲 HEARTWOOD ARTIFACT MAP 🌲
    ===========================
    """
    print(banner)

def format_map(file_path):
    if not os.path.exists(file_path):
        print(f"❌ Error: File {file_path} not found.")
        return

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Error parsing JSON: {e}")
        return

    print_banner()
    print(f"🆔 **Title:** {data.get('title', 'N/A')}")
    print(f"🔖 **Version:** {data.get('version', 'N/A')}")
    print(f"📝 **Description:** {data.get('description', 'N/A')}")
    print(f"⏰ **Generated At:** {data.get('generated_at', 'N/A')}")
    print("-" * 40)

    artifacts = data.get('artifacts', [])
    print(f"📂 **Total Artifacts Indexing:** {len(artifacts)}")
    print("")

    for art in artifacts:
        path = art.get('path', 'Unknown')
        status = art.get('status', 'unknown')
        last_review = art.get('last_human_review', 'never')
        tags = art.get('tags', [])
        
        status_emoji = "🟢" if status == "active" else "🟡" if status == "new" else "🔴"
        
        print(f"{status_emoji} **{path}**")
        print(f"   └─ 🕒 Last Reviewed: {last_review}")
        print(f"   └─ 🏷️  Tags: {', '.join(tags)}")
        print("")

    print("-" * 40)
    print(f"🖋️ **Attribution:** {data.get('attribution', 'Unknown')}")
    print("🌲 Stay rooted in the logic. 🌲")

if __name__ == "__main__":
    path = "repos/diy-make/memory/public/json/heartwood_map.json"
    if len(sys.argv) > 1:
        path = sys.argv[1]
    format_map(path)
