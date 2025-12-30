import os
import sys
import subprocess
import re
import argparse
from signatures.generate_salt import generate_salt_local

def main():
    parser = argparse.ArgumentParser(description="Universal Release Manager for versioned files in the metagit.")
    parser.add_argument("--agent-name", required=True, help="The name of the agent performing the release.")
    parser.add_argument("--agent-email", required=True, help="The email of the agent.")
    parser.add_argument("--repo-address", required=True, help="The path to the target repository.")
    parser.add_argument("--branch", required=True, help="The target branch in the repository.")
    parser.add_argument("--file-path", required=True, help="The relative path of the file to be versioned.")
    parser.add_argument("--version", required=True, help="The new MAJOR.MINOR.PATCH version number.")
    args = parser.parse_args()

    if not re.match(r"^\d+\.\d+\.\d+$", args.version):
        print(f"Error: Version '{args.version}' must be in the format MAJOR.MINOR.PATCH (e.g., 1.0.0)")
        sys.exit(1)

    print(f"--- Preparing V{args.version} Release for {args.file_path} ---")

    # 0. Check Remote Reachability
    print("Verifying remote reachability...")
    try:
        subprocess.run(['git', '-C', args.repo_address, 'ls-remote', '--exit-code', 'origin', 'HEAD'], capture_output=True, check=True)
        print("✔ Remote 'origin' is reachable.")
    except subprocess.CalledProcessError:
        print("❌ Error: Remote 'origin' is not reachable. Aborting release.")
        sys.exit(1)

    # 1. Generate Salt
    salt = generate_salt_local()
    full_version_string = f"V{args.version}_{salt}"
    print(f"Generated Salt: {salt}")
    print(f"Full Version String: {full_version_string}")

    # 2. Update the target file
    target_file_path = os.path.join(args.repo_address, args.file_path)
    try:
        with open(target_file_path, 'r') as f:
            content = f.read()
        
        new_content, count = re.subn(r"(__version__\s*=\s*)\".*\"", f"\\1\"{full_version_string}\"", content)
        
        if count == 0:
            print(f"Error: Could not find '__version__ = ...' string in '{target_file_path}'.")
            sys.exit(1)
            
        with open(target_file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated '{target_file_path}' with new version string.")

    except FileNotFoundError:
        print(f"Error: '{target_file_path}' not found.")
        sys.exit(1)

    # 3. Stage the change within the target repo
    original_directory = os.getcwd()
    try:
        os.chdir(args.repo_address)
        subprocess.run(['git', 'add', args.file_path], check=True)
        print(f"Staged '{args.file_path}' in repository '{args.repo_address}'.")
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error staging file: {e}")
        sys.exit(1)
    finally:
        os.chdir(original_directory)

    # 4. Perform the Release Commit
    filename = os.path.basename(args.file_path)
    commit_message = f"build({filename}): Release {full_version_string}"
    print(f"Performing release commit with message: '{commit_message}'")
    
    commit_script_path = "py/metagit_commit.py"
    
    try:
        subprocess.run([
            "python", commit_script_path,
            args.agent_name, args.agent_email, args.repo_address, args.branch, commit_message
        ], check=True)
        print("--- Release Commit Successful! ---")
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Error during commit process: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
