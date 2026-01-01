import json
import sys
import os

def format_json_todo(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    with open(file_path, 'r') as f:
        data = json.load(f)

    # Allow for both raw task lists and wedo_instance wrapped objects
    instance = data.get('wedo_instance', data)
    title = instance.get('title', instance.get('description', 'WeDo Task List'))
    print(f"# {title}\n")

    tasks = instance.get('tasks', [])
    for task in tasks:
        status = task.get('status', '[ ]')
        desc = task.get('description', 'No description')
        tid = task.get('id', 'N/A')
        print(f"{status} {tid} | {desc}")
        
        # Handle subtasks if present
        subtasks = task.get('subtasks', [])
        for sub in subtasks:
            s_status = sub.get('status', '[ ]')
            s_desc = sub.get('description', '')
            s_id = sub.get('id', '')
            print(f"  {s_status} {s_id} | {s_desc}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 py/format_todo.py <path_to_todo.json>")
    else:
        format_json_todo(sys.argv[1])
