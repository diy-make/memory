#!/usr/bin/env python3

import os
import sys
import json

# This is the "brick" - a simple function to create the markdown file
def create_image_markdown(image_filename, description):
    md_filename = os.path.splitext(image_filename)[0] + ".md"
    md_path = os.path.join(os.path.dirname(image_filename), md_filename)

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(f"# {image_filename}\n\n")
        f.write(f"![{description}]({os.path.basename(image_filename)})\n\n")
        f.write(f"*{description}*\n")

# This is the "metascript" definition
CHAIN = {
    "name": "Generate Image Descriptions with Human Verification",
    "description": "A chain that uses the agent's tools and a Python script to generate descriptions for images.",
    "steps": [
        {
            "name": "List Images",
            "tool": "list_directory",
            "args": {
                "dir_path": "repos/diy-make/memory/public/png"
            },
            "output": "image_files"
        },
        {
            "name": "Describe Images Loop",
            "loop_over": "image_files",
            "loop_variable": "image_file",
            "steps": [
                {
                    "name": "Get Image Description",
                    "tool": "read_file",
                    "args": {
                        "file_path": "{image_file.path}"
                    },
                    "output": "ai_description"
                },
                {
                    "name": "Get Human Feedback",
                    "tool": "human_prompt",
                    "prompt": "The AI description for {image_file.name} is: '{ai_description.description}'. Please provide a better description or press enter to accept.",
                    "output": "human_description"
                },
                {
                    "name": "Create Markdown File",
                    "tool": "run_shell_command",
                    "command": "python -c 'from __main__ import create_image_markdown; create_image_markdown(\"{image_file.path}\", \"{human_description}\")'"
                }
            ]
        }
    ]
}

# This is the "chain runner" logic
if __name__ == "__main__":
    # This is where the agent (me) would parse the CHAIN dictionary
    # and execute the steps. The logic would be similar to what I
    # proposed for the run_chain.py script.
    print("This script is a metascript and is meant to be executed by the agent.")
    print("To execute this chain, the agent will:")
    print("1. Read the CHAIN dictionary from this file.")
    print("2. Execute each step in the 'steps' array.")
    print("3. For the loop, it will iterate over the 'image_files' variable.")
    print("4. Inside the loop, it will call the 'read_file' tool, then prompt the human for feedback.")
    print("5. Finally, it will call the 'create_image_markdown' function defined in this script.")
