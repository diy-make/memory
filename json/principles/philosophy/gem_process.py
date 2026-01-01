import json
import sys
import os

def format_heartwood(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    with open(file_path, 'r') as f:
        data = json.load(f)

    title = data.get('title', 'Heartwood Record')
    version = data.get('version', '')
    description = data.get('description', '')
    
    if version:
        print(f"# {title} (Version {version})")
    else:
        print(f"# {title}")
        
    if description:
        print(f"{description}\n")

    # Handle Glossary terms
    if 'terms' in data:
        for item in data['terms']:
            term = item.get('term', 'Unknown')
            mod = item.get('modification', '')
            links = item.get('links', [])
            substrate = item.get('substrate', '')
            
            print(f"## {term}")
            if substrate:
                print(f"Substrate: {substrate}")
            print(f"Modification: {mod}")
            if links:
                print(f"Links: {', '.join(links)}")
            
            # Handle examples
            example = item.get('example')
            if example:
                print(f"\n### Successful Communication Example:")
                print(f"> \"{example.get('text', '')}\"")
                print(f"Context: {example.get('context', '')}")
                if example.get('artifact'):
                    print(f"Artifact: {example.get('artifact')}")
                if example.get('image'):
                    print(f"Image: {example.get('image')}")
            print("")

    # Handle generic key-value Heartwood
    elif 'heartwood_instance' in data or 'wedo_instance' in data:
        instance = data.get('heartwood_instance', data.get('wedo_instance'))
        for key, value in instance.items():
            if isinstance(value, list):
                print(f"## {key.replace('_', ' ').title()}")
                for item in value:
                    print(f"- {item}")
            elif isinstance(value, dict):
                print(f"## {key.replace('_', ' ').title()}")
                for k, v in value.items():
                    print(f"  **{k}:** {v}")
            else:
                print(f"**{key.replace('_', ' ').title()}:** {value}")
        print("")

    attribution = data.get('attribution', 'N/A')
    print(f"---\nSource: {file_path}\nAttribution: {attribution}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 py/format_heartwood.py <path_to_heartwood.json>")
    else:
        format_heartwood(sys.argv[1])
