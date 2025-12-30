import json
import datetime
import os
import argparse
import subprocess

def get_comms_dir():
    # The script is in repos/diy-make/memory/public/py/
    # local_paths.json is in repos/diy-make/memory/public/json/
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    paths_file = os.path.join(base_dir, "json", "local_paths.json")
    
    try:
        with open(paths_file, 'r') as f:
            paths = json.load(f)
            # The path in local_paths.json is "repos/diy-make/memory/comms/"
            # We need to resolve this relative to the gemini root.
            # But here we can just use the absolute path if we can find the gemini root.
            relative_comms = paths.get("local_paths", {}).get("swarm_comms")
            if relative_comms:
                # Find gemini root (where .venv is)
                current = base_dir
                while current != "/" and not os.path.exists(os.path.join(current, ".venv")):
                    current = os.path.dirname(current)
                return os.path.join(current, relative_comms)
    except Exception:
        pass
    
    # Fallback
    return os.path.abspath(os.path.join(base_dir, "..", "comms"))

def send_swarm_message(sender, recipient, message_type, content, file_paths=None, commit_hashes=None, other_relevant_info=None, pid=None, chat_log=None):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    
    if file_paths is None:
        file_paths = []
    if commit_hashes is None:
        commit_hashes = []
    if other_relevant_info is None:
        other_relevant_info = {}

    message = {
        "sender": sender,
        "recipient": recipient,
        "timestamp": timestamp,
        "message_type": message_type,
        "content": content,
        "context": {
            "file_paths": file_paths,
            "commit_hashes": commit_hashes,
            "other_relevant_info": other_relevant_info
        }
    }

    if message_type == "announcement" or message_type == "boot":
        if pid:
            message['pid'] = pid
        if chat_log:
            message['chat_log'] = chat_log
    else:
        if pid:
            message['context']['other_relevant_info']['pid'] = pid
        if chat_log:
            message['context']['other_relevant_info']['chat_log'] = chat_log

    file_name = f"{timestamp}_{sender}_to_{recipient}_{message_type}.json"
    comms_dir = get_comms_dir()
    file_path = os.path.join(comms_dir, file_name)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w") as f:
        json.dump(message, f, indent=2)

    print(f"Message sent to {recipient} in {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send a message to the swarm or a specific agent.")
    parser.add_argument("--sender", required=True, help="The name of the sending agent.")
    parser.add_argument("--recipient", required=True, help="The name of the recipient agent or 'swarm'.")
    parser.add_argument("--message_type", required=True, help="The type of message (e.g., communication, task_update, acknowledgment).")
    parser.add_argument("--content", required=True, help="The content of the message.")
    parser.add_argument("--file_paths", nargs='*', help="List of relevant file paths.")
    parser.add_argument("--commit_hashes", nargs='*', help="List of relevant commit hashes.")
    parser.add_argument("--other_relevant_info", type=json.loads, help="JSON string of other relevant information (e.g., '{\"key\": \"value\"}').")
    parser.add_argument("--pid", type=int, help="The process ID of the sending agent.")
    parser.add_argument("--chat_log", help="The path to the chat log file.")

    args = parser.parse_args()

    send_swarm_message(
        args.sender,
        args.recipient,
        args.message_type,
        args.content,
        args.file_paths,
        args.commit_hashes,
        args.other_relevant_info,
        args.pid,
        args.chat_log
    )