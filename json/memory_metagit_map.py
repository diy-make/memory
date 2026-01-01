import json
import sys
import os

def format_memory_map(file_path):
    if not os.path.exists(file_path):
        print(f"❌ Error: Map {file_path} not found.")
        return

    with open(file_path, 'r') as f:
        data = json.load(f)

    print(f"🌲 **Metagit Map: {data.get('title', 'Memory')}** 🌲")
    print(f"🆔 **Version:** {data.get('version', 'N/A')}")
    print(f"📂 **Root:** {data.get('root', 'N/A')}")
    print("=" * 45)

    mappings = data.get('mappings', [])
    for m in mappings:
        path = m.get('path', 'Unknown')
        m_type = m.get('type', 'data')
        status = m.get('status', 'active')
        
        icon = "🧠" if m_type == "heartwood" else "📹" if m_type == "substrate" else "📡" if m_type == "nerves" else "📂"
        status_color = "🔴" if status == "deprecated" else "🟢"
        
        print(f"{status_color} {icon} **{path}** ({m_type})")
        if m.get('description'):
            print(f"   └─ 📝 {m.get('description')}")
        if m.get('notes'):
            print(f"   └─ ⚠️ {m.get('notes')}")
        if m.get('contains'):
            print(f"   └─ 📦 Contains: {', '.join(m.get('contains'))}")
        print("")

    print("=" * 45)
    print(f"🖋️ **Attribution:** {data.get('attribution', 'Unknown')}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 py/format_memory_map.py <path_to_memory_map.json>")
    else:
        format_memory_map(sys.argv[1])
