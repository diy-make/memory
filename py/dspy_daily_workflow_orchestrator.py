import os
import subprocess
import shutil
from datetime import datetime, timedelta
import json

# Assuming DSPy modules are in the same directory or accessible via PYTHONPATH
# For this demonstration, we'll use a placeholder for DSPy interactions.

# Helper function to get the previous active day's date string (YYYY/Qx/MM/DD)
def get_previous_day_path(base_date=None):
    if base_date is None:
        base_date = datetime.now()
    
    # Adjust for previous day
    previous_date = base_date - timedelta(days=1)
    
    year = previous_date.year
    month = previous_date.month
    day = previous_date.day
    
    # Determine quarter
    if 1 <= month <= 3:
        quarter = "Q1"
    elif 4 <= month <= 6:
        quarter = "Q2"
    elif 7 <= month <= 9:
        quarter = "Q3"
    else:
        quarter = "Q4"
        
    return f"{year}/{quarter}/{month:02d}/{day:02d}"

# --- Main Orchestration Script ---
def orchestrate_daily_workflow(memory_repo_root, chat_repo_root, base_date=None):
    print("\n--- Starting DSPy Daily Workflow Orchestration ---")

    previous_day_path = get_previous_day_path(base_date)
    print(f"Processing logs for previous day: {previous_day_path}")

    # Define paths
    unclean_chat_dir = os.path.join(chat_repo_root, "unclean")
    reported_unclean_dir = os.path.join(chat_repo_root, "reported_unclean")
    memory_md_dir = os.path.join(memory_repo_root, previous_day_path, "md")
    memory_json_dir = os.path.join(memory_repo_root, previous_day_path, "json")

    # Ensure memory directories exist
    os.makedirs(memory_md_dir, exist_ok=True)
    os.makedirs(memory_json_dir, exist_ok=True)
    os.makedirs(reported_unclean_dir, exist_ok=True)

    # 1. Find uncleaned chat logs for the previous day
    previous_day_str_match = (base_date - timedelta(days=1)).strftime("%Y%m%d")
    uncleaned_logs = []
    for filename in os.listdir(unclean_chat_dir):
        if filename.startswith(previous_day_str_match) and filename.endswith(".txt"):
            uncleaned_logs.append(os.path.join(unclean_chat_dir, filename))
    
    if not uncleaned_logs:
        print(f"No uncleaned logs found for {previous_day_str_match}. Skipping daily reports.")
        return

    agent_summaries = []
    
    for log_file_path in uncleaned_logs:
        print(f"\nSummarizing log: {log_file_path}")
        
        # 2. Call the chat log summarization module (dspy_chat_summarizer.py)
        # For this demo, we'll call the Python script directly.
        try:
            # Need to pass the full path to the summarizer script
            summarizer_script = os.path.join(memory_repo_root, "py", "dspy_chat_summarizer.py")
            result = subprocess.run(
                ["./.venv/bin/python", summarizer_script, log_file_path],
                capture_output=True, text=True, check=True
            )
            print("Summarizer output (truncated):\n", result.stdout[:500]) # Print first 500 chars

            # Extract structured output (assuming the summarizer prints a JSON-like structure)
            # This part needs refinement to correctly parse the actual DSPy output
            extracted_summary = extract_summary_from_summarizer_output(result.stdout)
            if extracted_summary:
                agent_summaries.append(extracted_summary)

                # Save agent-specific markdown report
                agent_report_filename = f"{previous_day_str_match}_{extracted_summary['agent_name']}.md"
                agent_report_path = os.path.join(memory_md_dir, agent_report_filename)
                with open(agent_report_path, 'w', encoding='utf-8') as f:
                    f.write(generate_agent_report_markdown(extracted_summary))
                print(f"Generated agent report: {agent_report_path}")

                # Save agent-specific JSON data
                agent_json_filename = f"{previous_day_str_match}_{extracted_summary['agent_name']}.json"
                agent_json_path = os.path.join(memory_json_dir, agent_json_filename)
                with open(agent_json_path, 'w', encoding='utf-8') as f:
                    json.dump(extracted_summary, f, indent=2)
                print(f"Generated agent JSON: {agent_json_path}")
                
            else:
                print(f"Could not extract summary for {log_file_path}. Skipping agent report.")

            # Move the processed uncleaned chat log
            shutil.move(log_file_path, os.path.join(reported_unclean_dir, os.path.basename(log_file_path)))
            print(f"Moved {os.path.basename(log_file_path)} to reported_unclean.")

        except subprocess.CalledProcessError as e:
            print(f"Error summarizing log {log_file_path}: {e.stderr}")
        except Exception as e:
            print(f"An unexpected error occurred during log summarization: {e}")

    if not agent_summaries:
        print("No agent summaries successfully generated. Skipping daily summary.")
        return

    # 3. Call the daily summary generation module (dspy_daily_summary_generator.py)
    print("\nGenerating daily summary...")
    try:
        daily_summarizer_script = os.path.join(memory_repo_root, "py", "dspy_daily_summary_generator.py")
        
        # Prepare input for the daily summarizer
        temp_agent_summaries_file = os.path.join(memory_repo_root, "temp_agent_summaries.json")
        with open(temp_agent_summaries_file, 'w', encoding='utf-8') as f:
            json.dump(agent_summaries, f, indent=2)

        result = subprocess.run(
            ["./.venv/bin/python", daily_summarizer_script, temp_agent_summaries_file],
            capture_output=True, text=True, check=True
        )
        print("Daily summarizer output (truncated):\n", result.stdout[:500]) # Print first 500 chars
        
        # Extract the generated markdown (this needs to match the actual output of the DSPy module)
        daily_summary_markdown = extract_daily_summary_markdown(result.stdout)
        
        if daily_summary_markdown:
            daily_summary_path = os.path.join(memory_md_dir, "summary.md")
            with open(daily_summary_path, 'w', encoding='utf-8') as f:
                f.write(daily_summary_markdown)
            print(f"Generated daily summary: {daily_summary_path}")
        else:
            print("Could not extract daily summary markdown.")

        os.remove(temp_agent_summaries_file) # Clean up temp file

    except subprocess.CalledProcessError as e:
        print(f"Error generating daily summary: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred during daily summary generation: {e}")

    print("\n--- DSPy Daily Workflow Orchestration Complete ---")

def extract_summary_from_summarizer_output(output):
    """
    Parses the output of dspy_chat_summarizer.py to extract the structured summary.
    This is a placeholder and needs to be robustly implemented based on actual dspy output.
    """
    # Look for the "--- Extracted Chat Log Summary ---" block
    summary_start_marker = "--- Extracted Chat Log Summary ---"
    summary_end_marker_pattern = r"Agent Name:.*|start_date:.*|last_task_performed:.*|task_status:.*|tool_calls:.*|code_changes_additions:.*|code_changes_deletions:.*|wall_time:.*|agent_active:.*|api_time:.*|tool_time:.*|model_usage:.*"
    
    summary_block_match = re.search(f"{summary_start_marker}\s*\n(.*)", output, re.DOTALL)
    if not summary_block_match:
        print("Warning: Summary block not found in summarizer output.")
        return None
    
    summary_text = summary_block_match.group(1)
    
    extracted_data = {}
    
    # Extract each line that starts with a key
    lines = summary_text.strip().split('\n')
    for line in lines:
        parts = line.split(':', 1)
        if len(parts) == 2:
            key = parts[0].strip()
            value = parts[1].strip()
            
            # Convert keys to match JSON structure expected by ChatLogSummary
            if key == "agent_name": extracted_data["agent_name"] = value
            elif key == "start_date": extracted_data["start_date"] = value
            elif key == "last_task_performed": extracted_data["last_task_performed"] = value
            elif key == "task_status": extracted_data["task_status"] = value
            elif key == "tool_calls": extracted_data["tool_calls"] = int(value)
            elif key == "code_changes_additions": extracted_data["code_changes_additions"] = int(value)
            elif key == "code_changes_deletions": extracted_data["code_changes_deletions"] = int(value)
            elif key == "wall_time": extracted_data["wall_time"] = value
            elif key == "agent_active": extracted_data["agent_active"] = value
            elif key == "api_time": extracted_data["api_time"] = value
            elif key == "tool_time": extracted_data["tool_time"] = value
            elif key == "model_usage": 
                try:
                    extracted_data["model_usage"] = json.loads(value)
                except json.JSONDecodeError:
                    extracted_data["model_usage"] = [] # Fallback for malformed JSON
    
    return extracted_data

def generate_agent_report_markdown(summary_dict):
    """Generates markdown content for an individual agent's report."""
    markdown = f"# Session Analysis: {summary_dict['start_date']} - {summary_dict['agent_name']}\n\n"
    markdown += f"## Agent Identification\n\n"
    markdown += f"-   **Agent Name:** {summary_dict['agent_name']}\n"
    markdown += f"\n## Session Analysis\n\n"
    markdown += f"-   **Start Date:** {summary_dict['start_date']}\n"
    markdown += f"-   **Last Task:** {summary_dict['last_task_performed']}\n"
    markdown += f"-   **Task Status:** {summary_dict['task_status']}\n"
    markdown += f"\n## Quantitative Summary\n\n"
    markdown += f"-   **Tool Calls:** {summary_dict['tool_calls']}\n"
    markdown += f"-   **Code Changes:** +{summary_dict['code_changes_additions']} -{summary_dict['code_changes_deletions']}\n"
    markdown += f"-   **Wall Time:** {summary_dict['wall_time']}\n"
    markdown += f"-   **Agent Active:** {summary_dict['agent_active']}\n"
    markdown += f"-   **API Time:** {summary_dict['api_time']}\n"
    markdown += f"-   **Tool Time:** {summary_dict['tool_time']}\n"
    markdown += f"\n## Model Usage\n\n```json\n{json.dumps(summary_dict['model_usage'], indent=2)}\n```\n"
    return markdown

def extract_daily_summary_markdown(output):
    """
    Parses the output of dspy_daily_summary_generator.py to extract the markdown.
    """
    summary_start_marker = "--- Simulated Daily Summary Markdown Output ---"
    summary_block_match = re.search(f"{summary_start_marker}\s*\n(.*)", output, re.DOTALL)
    if summary_block_match:
        return summary_block_match.group(1).strip()
    return None

if __name__ == "__main__":
    # Define root paths relative to where this script is executed
    # This script is in repos/diy-make/memory/py/
    # memory_repo_root is repos/diy-make/memory/
    # chat_repo_root is gemini/.chat/ (from gemini root)
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    memory_repo_root = os.path.dirname(current_script_dir) # Should be repos/diy-make/memory/
    
    # Need to go up from memory_repo_root (repos/diy-make/memory/) to gemini root, then into .chat/
    gemini_root = os.path.abspath(os.path.join(memory_repo_root, os.pardir, os.pardir, os.pardir))
    chat_repo_root = os.path.join(gemini_root, ".chat")
    
    # For demonstration purposes, let's assume 'today' is 2025-12-12 for testing previous day's logs (2025-12-11)
    # In a live agent, this would typically be `datetime.now()`
    orchestrate_daily_workflow(memory_repo_root, chat_repo_root, base_date=datetime(2025, 12, 12))
