import json
import sys
import os

def format_heartwood(file_path):
    """
    Universal formatter for Metagit Heartwood JSON files.
    Identifies and renders various schemas (principles, virtues, rules, glossary, todo).
    """
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in {file_path}")
        return

    # 1. Metadata Extraction
    title = data.get('title', os.path.basename(file_path))
    version = data.get('version', data.get('v', ''))
    description = data.get('description', '')
    attribution = data.get('attribution', 'N/A')

    print(f"\n# {title}" + (f" (V{version})" if version else ""))
    if description:
        print(f"{description}\n")

    # 2. Schema-Specific Rendering
    
    # Handle Glossary terms
    if 'terms' in data:
        for item in data['terms']:
            term = item.get('term', 'Unknown')
            mod = item.get('modification', '')
            substrate = item.get('substrate', '')
            print(f"## {term}")
            if substrate: print(f"Substrate: {substrate}")
            if mod: print(f"Modification: {mod}")
            
            example = item.get('example')
            if example:
                print(f"### Example:\n> \"{example.get('text', '')}\"\nContext: {example.get('context', '')}")
            print("")

    # Handle Lists (virtues, principles, rules, tasks)
    for key in ['values', 'virtues', 'principles', 'rules', 'tasks', 'steps', 'improvements']:
        if key in data and isinstance(data[key], list):
            print(f"## {key.title()}")
            for item in data[key]:
                if isinstance(item, dict):
                    name = item.get('name', item.get('title', item.get('id', '')))
                    rule = item.get('rule', item.get('description', ''))
                    status = item.get('status', '')
                    
                    line = f"- "
                    if status: line += f"{status} "
                    if name: line += f"**{name}**: "
                    line += rule
                    print(line)
                    
                    # Handle sub-lists if present
                    for sub_key in ['sub_tasks', 'subtasks', 'sub_principles', 'procedure']:
                        if sub_key in item and isinstance(item[sub_key], list):
                            for sub in item[sub_key]:
                                if isinstance(sub, dict):
                                    s_name = sub.get('name', sub.get('id', ''))
                                    s_rule = sub.get('rule', sub.get('description', ''))
                                    s_status = sub.get('status', '')
                                    print(f"  - {s_status} {s_name}: {s_rule}".strip())
                                else:
                                    print(f"  - {sub}")
                else:
                    print(f"- {item}")
            print("")

    # Handle Generic Key-Value structures
    if 'content' in data and isinstance(data['content'], dict):
        for k, v in data['content'].items():
            print(f"## {k.replace('_', ' ').title()}")
            if isinstance(v, dict):
                for sub_k, sub_v in v.items():
                    print(f"  **{sub_k.title()}**: {sub_v}")
            else:
                print(v)
            print("")

    # Handle Wrapped Instances (heartwood_instance, wedo_instance)
    for wrap in ['heartwood_instance', 'wedo_instance']:
        if wrap in data and isinstance(data[wrap], dict):
            instance = data[wrap]
            for k, v in instance.items():
                if k in ['title', 'description', 'attribution', 'version']: continue
                print(f"## {k.replace('_', ' ').title()}")
                if isinstance(v, list):
                    for i in v: print(f"- {i}")
                elif isinstance(v, dict):
                    for sk, sv in v.items(): print(f"  **{sk.title()}**: {sv}")
                else:
                    print(v)
            print("")

    print(f"---\nSource: {file_path}\nAttribution: {attribution}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 py/format_heartwood.py <path_to_json>")
    else:
        format_heartwood(sys.argv[1])