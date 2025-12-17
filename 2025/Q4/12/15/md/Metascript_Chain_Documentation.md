# Metascript Chain Documentation

This document outlines the structure and usage of our JSON-based "metascript" files, which are designed to create complex chains of operations for me, the AI agent, to execute.

## What is a Metascript?

A metascript is a JSON file that defines a sequence of steps for me to perform a task. It is a machine-readable "script" for me, the agent, to follow. Each metascript file is a single "chain" of operations.

## Why use JSON Schema?

We are using the JSON Schema standard (draft-04) to define the structure of our metascript files. This provides several key advantages:

*   **Validation:** We can automatically validate our metascript files to ensure they are correctly structured.
*   **Clear Contract:** The schema provides a clear, unambiguous contract for what a valid metascript looks like.
*   **Machine-Readability:** The schema is machine-readable, which allows me to understand and execute the chain.
*   **Documentation:** The schema itself serves as a form of documentation.

Each metascript file will reference our master schema using the `$schema` keyword.

## The "Brick" and "Mortar" Analogy

Our metascript system is based on the "brick" and "mortar" analogy:

*   **Bricks:** These are the individual, self-contained scripts that perform a specific task (e.g., a Python script, a shell script).
*   **Mortar:** This is my LLM environment, which includes my built-in tools (`read_file`, `list_directory`, etc.) and my ability to orchestrate the execution of the "bricks".

The metascript file is the blueprint that tells me how to use the mortar to assemble the bricks into a complete structure.

## The Metascript Schema

Here is the proposed JSON Schema for our metascript files. This new version incorporates the "Human-in-the-Loop" concept, allowing the chain to prompt for human input.

```json
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "Metascript Chain",
    "description": "A schema for defining a chain of agent operations, including human-in-the-loop steps.",
    "type": "object",
    "properties": {
        "name": {
            "description": "The name of the metascript.",
            "type": "string"
        },
        "description": {
            "description": "A description of what the metascript does.",
            "type": "string"
        },
        "steps": {
            "type": "array",
            "items": {
                "oneOf": [
                    { "$ref": "#/definitions/action_step" },
                    { "$ref": "#/definitions/loop_step" }
                ]
            }
        }
    },
    "required": ["name", "description", "steps"],
    "definitions": {
        "action_step": {
            "type": "object",
            "properties": {
                "name": {
                    "description": "The name of the step.",
                    "type": "string"
                },
                "tool": {
                    "description": "The tool to call. Can be an agent tool, shell command, or 'human_prompt'.",
                    "type": "string"
                },
                "prompt": {
                    "description": "The prompt to display to the human if the tool is 'human_prompt'.",
                    "type": "string"
                },
                "args": {
                    "description": "The arguments for the tool.",
                    "type": "object"
                },
                "output": {
                    "description": "The name of the variable to store the tool's output.",
                    "type": "string"
                }
            },
            "required": ["name", "tool"]
        },
        "loop_step": {
            "type": "object",
            "properties": {
                "name": {
                    "description": "The name of the loop.",
                    "type": "string"
                },
                "loop_over": {
                    "description": "The name of the variable to loop over.",
                    "type": "string"
                },
                "loop_variable": {
                    "description": "The name of the variable for each item in the loop.",
                    "type": "string"
                },
                "steps": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/action_step"
                    }
                }
            },
            "required": ["name", "loop_over", "steps"]
        }
    }
}
```

## Example: `image_description.json` with Human-in-the-Loop

This example demonstrates how a human can be included in the chain to verify or provide input.

```json
{
    "$schema": "./schemas/metascript.schema.json",
    "name": "Generate Image Descriptions with Human Verification",
    "description": "A chain that uses the agent's tools and a human to generate and verify descriptions for images.",
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
                    "name": "Generate AI Description",
                    "tool": "read_file",
                    "args": {
                        "file_path": "{image_file}"
                    },
                    "output": "ai_description"
                },
                {
                    "name": "Get Human Feedback",
                    "tool": "human_prompt",
                    "prompt": "The AI description for {image_file} is: '{ai_description.description}'. Please provide a better description or press enter to accept.",
                    "output": "human_description"
                },
                {
                    "name": "Create Markdown File",
                    "tool": "run_shell_command",
                    "command": "python repos/diy-make/memory/public/py/create_image_markdown.py '{image_file}' '{human_description}'"
                }
            ]
        }
    ]
}
```

## How to Execute a Metascript

To execute a metascript, I will need a "chain runner" script. This will be a Python script (`run_chain.py`) that does the following:

1.  Takes the path to a `.json` metascript file as an argument.
2.  Parses the JSON file.
3.  Optionally validates the file against our `metascript.schema.json`.
4.  Executes each step in the `steps` array in order.
5.  Handles loops and variable substitutions.

This new system provides a powerful and extensible way for us to create complex workflows.
