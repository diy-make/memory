import json
import os
import argparse
import subprocess
import glob

def get_comms_dir():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    paths_file = os.path.join(base_dir, "json", "local_paths.json")
    try:
        with open(paths_file, 'r') as f:
            paths = json.load(f)
            relative_comms = paths.get("local_paths", {}).get("swarm_comms")
            if relative_comms:
                current = base_dir
                while current != "/" and not os.path.exists(os.path.join(current, ".venv")):
                    current = os.path.dirname(current)
                return os.path.join(current, relative_comms)
    except Exception:
        pass
    return os.path.abspath(os.path.join(base_dir, "..", "comms"))

def get_processed_messages_file():
    # Store processed list in the comms directory itself or a sibling
    comms_dir = get_comms_dir()
    return os.path.join(comms_dir, ".processed_messages.txt")

def get_processed_messages():
    processed_file = get_processed_messages_file()
    if not os.path.exists(processed_file):
        return set()
    with open(processed_file, "r") as f:
        return set(f.read().splitlines())

def add_processed_message(message_filename):
    processed_file = get_processed_messages_file()
    with open(processed_file, "a") as f:
        f.write(message_filename + "\n")

def read_swarm_messages(agent_name=None):
    comms_dir = get_comms_dir()
    if not os.path.exists(comms_dir):
        print(f"Communication directory '{comms_dir}' does not exist.")
        return

    processed_messages = get_processed_messages()
    new_messages = []
    
    # Scan for all JSON files in the comms directory
    candidate_files = glob.glob(os.path.join(comms_dir, "*.json"))

    for file_path in candidate_files:
        filename = os.path.basename(file_path)
        if filename not in processed_messages:
            try:
                with open(file_path, "r") as f:
                    message = json.load(f)
                    
                    # Filter by recipient if agent_name is provided
                    recipient = message.get('recipient', 'swarm').lower()
                    if agent_name:
                        target = agent_name.lower()
                        if recipient != target and recipient != 'swarm':
                            continue
                    
                    # Filter out messages sent by the current agent
                    if agent_name and message.get('sender', '').lower() == agent_name.lower():
                        continue
                        
                    new_messages.append((filename, message))
            except json.JSONDecodeError:
                print(f"Warning: Could not decode JSON from {filename}")
    
    if not new_messages:
        print("No new messages.")
        return

    for filename, message in new_messages:
        print(f"--- New Message from {message.get('sender', 'Unknown')} ---")
        print(f"  Recipient: {message.get('recipient', 'Unknown')}")
        print(f"  Timestamp: {message.get('timestamp', 'Unknown')}")
        print(f"  Type: {message.get('message_type', 'Unknown')}")
        print(f"  Content: {message.get('content', 'No Content')}")
        
        context = message.get('context', {})
        if context:
            if context.get('file_paths'):
                print(f"  Context - File Paths: {', '.join(context['file_paths'])}")
            if context.get('commit_hashes'):
                print(f"  Context - Commit Hashes: {', '.join(context['commit_hashes'])}")
            if context.get('other_relevant_info'):
                print(f"  Context - Other Info: {json.dumps(context['other_relevant_info'])}")
        print("------------------------------------")
        
        add_processed_message(filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read messages from the swarm.")
    parser.add_argument("--agent-name", help="Filter messages for a specific agent.")
    args = parser.parse_args()
    read_swarm_messages(args.agent_name)