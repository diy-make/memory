import dspy
import re
import json

# --- DSPy Configuration (placeholder) ---
# In a real scenario, configure your language model here.
# For example:
# turbo = dspy.OpenAI(model='gpt-3.5-turbo')
# dspy.configure(lm=turbo)

# --- DSPy Signature ---
class ChatLogSummary(dspy.Signature):
    """
    Summarizes a raw chat log, extracting key information about an AI agent's 
session.
    The raw chat log may contain terminal escape codes and other noise.
    """
    raw_chat_log = dspy.InputField(desc="The raw, uncleaned chat log content.")
    
    agent_name = dspy.OutputField(desc="The identified name of the AI agent for this session (e.g., Kore, Solara). If not explicitly found, use 'Unnamed'.")
    start_date = dspy.OutputField(desc="The start date of the session in YYYY-MM-DD format. Extract from the 'Script started on YYYY-MM-DD HH:MM:SS' line.")
    last_task_performed = dspy.OutputField(desc="A concise summary of the last significant task the agent was working on.")
    task_status = dspy.OutputField(desc="The status of the last task (e.g., 'Completed', 'Interrupted by API Error', 'Terminated by User', 'No Active Task').")
    tool_calls = dspy.OutputField(desc="Total number of tool calls made in the session (integer). If not found, use 0.")
    code_changes_additions = dspy.OutputField(desc="Total lines of code added (integer, e.g., '+123'). If not found, use 0.")
    code_changes_deletions = dspy.OutputField(desc="Total lines of code deleted (integer, e.g., '-45'). If not found, use 0.")
    wall_time = dspy.OutputField(desc="Total wall time of the session (e.g., '20h 41m 5s'). If not found, use 'N/A'.")
    agent_active = dspy.OutputField(desc="Total time agent was active (e.g., '7h 8m 12s'). If not found, use 'N/A'.")
    api_time = dspy.OutputField(desc="Total API time (e.g., '5h 16m 8s (73.8%)'). If not found, use 'N/A'.")
    tool_time = dspy.OutputField(desc="Total tool time (e.g., '1h 52m 4s (26.2%)'). If not found, use 'N/A'.")
    
    model_usage = dspy.OutputField(desc="JSON string array of model usage objects, each with 'model_name', 'requests', 'input_tokens', 'output_tokens'. Example: [{'model_name': 'gemini-2.5-flash-lite', 'requests': 2545, 'input_tokens': 2834116, 'output_tokens': 16407}]. If not found, use an empty array '[]'.")

# --- DSPy Module ---
class ChatSummarizer(dspy.Module):
    def __init__(self):
        super().__init__()
        self.predict = dspy.Predict(ChatLogSummary)

    def forward(self, raw_chat_log):
        return self.predict(raw_chat_log=raw_chat_log)

# --- Helper function for text cleaning and extraction (non-DSPy) ---
def clean_and_extract_info(raw_log_content):
    """
    Attempts to extract structured information from a raw chat log using regex.
    This is a non-DSPy helper to pre-process the raw log or provide fallback.
    """
    info = {
        "agent_name": "Unnamed",
        "start_date": "N/A",
        "last_task_performed": "N/A",
        "task_status": "N/A",
        "tool_calls": 0,
        "code_changes_additions": 0,
        "code_changes_deletions": 0,
        "wall_time": "N/A",
        "agent_active": "N/A",
        "api_time": "N/A",
        "tool_time": "N/A",
        "model_usage": "[]"
    }

    # Normalize line endings and remove problematic terminal characters
    raw_log_content = re.sub(r'\r\n|\r', '\n', raw_log_content)
    raw_log_content = re.sub(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]|[\u2500-\u256F\u2580-\u259F\u25A0-\u25FF]', '', raw_log_content)

    # Normalize line endings and remove problematic terminal characters
    raw_log_content = re.sub(r'\r\n|\r', '\n', raw_log_content)
    raw_log_content = re.sub(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]|[\u2500-\u256F\u2580-\u259F\u25A0-\u25FF]', '', raw_log_content)

    print(f"--- Raw Log Content (after cleaning) ---\n{raw_log_content[:500]}...")

    # Extract start date
    date_match = re.search(r"Script started on (\d{4}-\d{2}-\d{2})", raw_log_content)
    if date_match:
        info["start_date"] = date_match.group(1)

    # Extract agent name from screen title or explicit statement
    name_match = re.search(r"screen -X title \"(.*?)\"", raw_log_content)
    if name_match:
        info["agent_name"] = name_match.group(1)
    else:
        name_match = re.search(r"Agent Name:\s*(.*?)\s*\n", raw_log_content)
        if name_match and name_match.group(1).strip() != "Unnamed":
            info["agent_name"] = name_match.group(1).strip()
    
    # Extract Tool Calls
    tool_calls_match = re.search(r"Tool Calls:\s*(\d+)", raw_log_content)
    if tool_calls_match:
        info["tool_calls"] = int(tool_calls_match.group(1))

    # Extract Code Changes
    code_changes_add_match = re.search(r"Code Changes:\s*\+(\d+)", raw_log_content)
    if code_changes_add_match:
        info["code_changes_additions"] = int(code_changes_add_match.group(1))
    code_changes_del_match = re.search(r"Code Changes:.*?-\s*(\d+)", raw_log_content)
    if code_changes_del_match:
        info["code_changes_deletions"] = int(code_changes_del_match.group(1))

    # Extract Wall Time
    wall_time_match = re.search(r"Wall Time:(.*)", raw_log_content)
    if wall_time_match:
        info["wall_time"] = wall_time_match.group(1).strip()

    # Extract Agent Active Time
    agent_active_match = re.search(r"Agent Active:\s*(.*?)(?=\s*\n)", raw_log_content)
    if agent_active_match:
        info["agent_active"] = agent_active_match.group(1).strip()

    # Extract API Time
    api_time_match = re.search(r"API Time:\s*(.*?)(?=\s*\n)", raw_log_content)
    if api_time_match:
        info["api_time"] = api_time_match.group(1).strip()

    # Extract Tool Time
    tool_time_match = re.search(r"Tool Time:\s*(.*?)(?=\s*\n)", raw_log_content)
    if tool_time_match:
        info["tool_time"] = tool_time_match.group(1).strip()

    # Extract Model Usage
    model_usage_data = []
    model_usage_block_match = re.search(r"Model Usage\s*-----+(.*?)-----", raw_log_content, re.DOTALL)
    if model_usage_block_match:
        model_usage_text = model_usage_block_match.group(1)
        model_lines = re.findall(r"(gemini-\S+)\s+(\d+)\s+([\d,]+)\s+([\d,]+)", model_usage_text)
        for model_name, reqs, input_tokens, output_tokens in model_lines:
            model_usage_data.append({
                "model_name": model_name,
                "requests": int(reqs),
                "input_tokens": int(input_tokens.replace(",", "")),
                "output_tokens": int(output_tokens.replace(",", ""))
            })
    if model_usage_data:
        info["model_usage"] = json.dumps(model_usage_data)

    # Simplified extraction for last_task and task_status from the text
    # This might require more sophisticated NLP for accurate extraction in real DSPy
    last_task_match = re.search(r"Last Task:\s*(.*?)(?=\n\s*Task Status:)", raw_log_content, re.DOTALL)
    if last_task_match:
        info["last_task_performed"] = last_task_match.group(1).strip()
    
    task_status_match = re.search(r"Task Status:\s*(.*?)(?=\n\s*Interaction Summary:|\n\s*## Session Log)", raw_log_content, re.DOTALL)
    if task_status_match:
        info["task_status"] = task_status_match.group(1).strip()

    return info

# --- Main function for demonstration ---
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Summarize a raw chat log using DSPy.")
    parser.add_argument("log_file_path", type=str, help="Path to the raw chat log file.")
    args = parser.parse_args()

    # Read the raw chat log content
    try:
        with open(args.log_file_path, 'r', encoding='utf-8') as f:
            raw_log_content = f.read()
    except FileNotFoundError:
        print(f"Error: Log file not found at {args.log_file_path}")
        exit(1)
    except Exception as e:
        print(f"Error reading log file: {e}")
        exit(1)

    # Initialize the DSPy module (without a real LM for this demo)
    summarizer = ChatSummarizer()

    # For a real DSPy run, you'd use:
    # prediction = summarizer.forward(raw_chat_log=raw_log_content)

    # For this demo, we'll use the helper function as a stand-in for the DSPy LM's output
    # or to pre-process for a more focused DSPy call.
    prediction_dict = clean_and_extract_info(raw_log_content)

    print("\n--- Extracted Chat Log Summary ---")
    for key, value in prediction_dict.items():
        if key == "model_usage":
            print(f"{key}: {json.dumps(json.loads(value), indent=2)}")
        else:
            print(f"{key}: {value}")

    # Example of how you would use the DSPy output fields
    # print(f"Agent Name: {prediction.agent_name}")
    # print(f"Start Date: {prediction.start_date}")
    # ... and so on for other fields