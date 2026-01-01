import json
import sys
import os

def format_review(file_path):
    if not os.path.exists(file_path):
        print(f"❌ Error: Review log {file_path} not found.")
        return

    with open(file_path, 'r') as f:
        data = json.load(f)

    print(f"📓 **Audit Log:** {data.get('title', 'JSON Review')}")
    print(f"👤 **Agent:** {data.get('agent', 'Unknown')}")
    print(f"🆔 **Session:** {data.get('session_id', 'N/A')}")
    print("=" * 40)

    entries = data.get('entries', [])
    for entry in entries:
        print(f"🔍 **Entry {entry.get('id', '??')}:** {entry.get('path', 'Unknown')}")
        print(f"   ├─ ✅ **Decision:** {entry.get('decision', 'Pending')}")
        print(f"   ├─ 💡 **Rationale:** {entry.get('rationale', 'N/A')}")
        print(f"   ├─ 👤 **User Input:** {entry.get('user_reasons', 'None')}")
        
        flags = entry.get('flags', [])
        if flags:
            print(f"   ├─ 🚩 **Flags:** {', '.join(flags)}")
        
        print(f"   └─ 🚀 **Recommendation:** {entry.get('recommendation', 'N/A')}")
        print("")

    tasks = data.get('wedo_tasks', [])
    if tasks:
        print("📝 **New WeDo Tasks:**")
        for task in tasks:
            print(f"   - [ ] {task}")

    print("=" * 40)
    print("🌲 Review synchronized with Heartwood. 🌲")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 py/format_json_review.py <path_to_audit.json>")
    else:
        format_review(sys.argv[1])
