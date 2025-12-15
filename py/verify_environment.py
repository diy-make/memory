import os
import sys
import subprocess

# The version of the environment configuration this script validates.
__version__ = "1.0.0"

def check_directory(path, must_exist=True):
    """Checks for the existence of a directory."""
    if os.path.isdir(path):
        print(f"✔ Directory '{path}' found.")
        return True
    else:
        if must_exist:
            print(f"❌ Core directory '{path}' not found.")
        return False

def verify_public_memory_environment():
    """
    Verifies the integrity of the public memory module environment.
    """
    print(f"--- Verifying Public Memory Environment v{__version__} ---")
    all_ok = True
    project_root = os.getcwd()

    # 1. Check Virtual Environment
    print("\n[1/3] Checking Virtual Environment...")
    expected_python_path = os.path.join(project_root, '.venv/bin/python')
    if sys.executable == expected_python_path:
        print(f"✔ Using correct virtual environment.")
    else:
        # We can't guarantee .venv exists if this check fails, so don't assume.
        print(f"❌ Not running with this repository's venv.")
        all_ok = False

    # 2. Check Top-Level Directory Structure
    print("\n[2/3] Checking Top-Level Directory Structure...")
    core_dirs = ["json", "md", "py"]
    for directory in core_dirs:
        if not check_directory(directory):
            all_ok = False
            
    # 3. Check JSON Directory Structure
    print("\n[3/3] Checking JSON Directory Structure...")
    json_dirs = [
        "json/agent_protocols",
        "json/configuration",
        "json/design_principles",
        "json/domain_specific_knowledge",
        "json/git_protocols",
        "json/learnings",
        "json/personality",
        "json/project_architecture",
        "json/project_management",
        "json/rules",
        "json/schema",
        "json/universal"
    ]
    for directory in json_dirs:
        if not check_directory(directory):
            all_ok = False

    print("\n--- Verification Complete ---")
    if all_ok:
        print("✅ Public memory foundational structure is correct.")
    else:
        print("❌ Public memory has configuration issues. Please address the errors above.")
    
    return all_ok

if __name__ == '__main__':
    if not verify_public_memory_environment():
        sys.exit(1)
