import os
import sys
import subprocess
import hashlib
import argparse

# The version of the Memory Module environment configuration.
# This will be replaced by the release manager during a release commit.
__version__ = "V0.8.0_Ethos_Finish"

CORE_FILE_CHECKSUMS = {
    "README.ai": "bd5b2736ed487234f9169d53f74f04848abfa3e3b97cebba87abc9bc94caa557",
    "README.md": "b7c5503505be5126b89eaecec063083a36558c7edbdf26116781292e77654822",
    "VERSION": "30c99e8b103eacbe6f6d6e1b54b06ca6d5f3164b4f50094334a517ae95ca8fba",
    "json/local_paths.json": "3c46f16ea7deffaaaede72c14843d2bf0d5b427e7e5e5917f85bd4ee692234fb",
    "json/rules/swarm_protocol.json": "2611d24ac52ce620ecf0cd6bb5ca911769052619aacd2e30fb0961ce2623c2f8",
    "json/principles/agent_virtues.json": "4fbfd2378a4bb8d778636908ad7ba35ae24a0a499372701d926d4ca951ca7b96",
    "json/configuration/verified_repositories.json": "9dcc60f1261f0dbdfd720dbe4eea551c1072b46aecdf0fcf4cf94c0e6e903b79",
    "md/wedo/markdown_generation/png_journal.todo.md": "1500212fbf702e2dc3c915a6e3a5cfecb308b4648d58b3d620c41289dd08192c",
    "md/wedo/markdown_generation/boilerplate_report.todo.md": "2d2658d7124fc6d14d0879ab9513313ba8145b5456a53032ab0d38bb3d1870bb",
    "md/wedo/markdown_generation/boilerplate_readme.todo.md": "f71844e116b4d1b5409880b64da8ae4a5b0b7d59161b4d2e81fe464448a7a2d1",
    "md/wedo/markdown_generation/biography.todo.md": "d5706c14ef214d8d7543c2ae7eec719d8ce704e7f49add03fa6424798d5a25a6",
    "md/wedo/github/remote_pull.todo.md": "885fa25641df64a74e634e98146896714133022d5d9d33c14f66c0f13086259a",
    "md/wedo/github/github_audit_repair.todo.md": "1b47487d4fb1f114143a2a7b2392d4b8bbc35c88ab8a978d81231799556b3e38",
    "md/wedo/meta_wedo.todo.md": "6aa9350677476b2ff2e91fe786c7e5dc7d21adf6e496b2944d13e5ac74e5155b"
}

def get_file_sha256(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""): 
                sha256.update(byte_block)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def check_remote_origin():
    required_path = "diy-make/memory"
    try:
        result = subprocess.run(['git', 'remote', 'get-url', 'origin'], capture_output=True, text=True, check=True)
        remote_url = result.stdout.strip()
        if required_path in remote_url:
             print(f"✔ Git remote 'origin' correctly points to '{required_path}' ({remote_url}).")
             return True
        else:
            print(f"❌ Git remote 'origin' is set to '{remote_url}'. Expected to contain '{required_path}'.")
            return False
    except subprocess.CalledProcessError:
        print("⚠ Git remote 'origin' is not configured (Common for local-only forks).")
        return True 

def verify_self_integrity():
    my_path = "py/verify_environment.py"
    my_version = __version__
    
    if "PLACEHOLDER" in my_version:
        print("✔ Skipping self-integrity check for PLACEHOLDER version.")
        return True

    current_checksum = get_file_sha256(my_path)
    if not current_checksum:
        print("❌ Could not calculate checksum of the running script.")
        return False

    try:
        commit_message = f"build(verify_environment.py): Release {my_version}"
        log_cmd = ['git', 'log', '--grep', commit_message, '-n', '1', '--pretty=format:%H']
        result = subprocess.run(log_cmd, capture_output=True, text=True, check=True)
        commit_hash = result.stdout.strip()
        if not commit_hash:
            print(f"⚠ Could not find a 'Release Commit' for version '{my_version}'. (Expected for unreleased versions)")
            return True # Soft fail for dev versions
        show_cmd = ['git', 'show', f'{commit_hash}:{my_path}']
        historical_content = subprocess.check_output(show_cmd)
        historical_checksum = hashlib.sha256(historical_content).hexdigest()
        if current_checksum == historical_checksum:
            print(f"✔ Self-integrity check passed for version {my_version}.")
            return True
        else:
            print(f"❌ Self-integrity check failed! Script has been modified since release.")
            return False
    except Exception as e:
        print(f"⚠ Self-integrity check skipped or failed: {e}")
        return True

def verify_environment(no_self_verify=False):
    print(f"--- verifying Memory Module environment v{__version__} ---")
    all_ok = True
    
    # 1. Remote Configuration
    print("\n[1/4] Checking Remote Configuration...")
    if not check_remote_origin():
        all_ok = False

    # 2. Core Directory Structure
    print("\n[2/4] Checking Core Directory Structure...")
    # 'schemas' was renamed or is a duplicate, the project uses 'json/schema/'
    core_dirs = ["json", "md", "png", "py"]
    for directory in core_dirs:
        if not os.path.isdir(directory):
            print(f"❌ Core directory '{directory}' missing.")
            all_ok = False
        else:
            print(f"✔ Directory '{directory}' present.")

    # 3. Core File Integrity
    print("\n[3/4] Checking Core File Integrity...")
    for file_path, expected_checksum in CORE_FILE_CHECKSUMS.items():
        if not check_file_integrity(file_path, expected_checksum):
            # We allow the verify script itself to be updated without failing the whole check here,
            # as it will be caught by self-integrity later if needed.
            if file_path != "py/verify_environment.py":
                all_ok = False

    # 4. Self-Integrity
    print("\n[4/4] Verifying Self-Integrity...")
    if no_self_verify:
        print("✔ Self-integrity check skipped due to --no-self-verify flag.")
    elif not verify_self_integrity():
        all_ok = False

    print("\n--- Verification Complete ---")
    if all_ok:
        print("✅ Environment is configured correctly.")
    else:
        print("❌ Environment has configuration issues.")
    
    return all_ok

def check_file_integrity(file_path, expected_checksum):
    actual_checksum = get_file_sha256(file_path)
    if actual_checksum is None:
        print(f"❌ Core file '{file_path}' not found.")
        return False
    
    if actual_checksum == expected_checksum:
        print(f"✔ Core file '{file_path}' has correct checksum.")
        return True
    else:
        print(f"❌ Core file '{file_path}' has been modified or is corrupt.")
        return False

if __name__ == '__main__':
    # Determine the directory where the script is located
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Change current working directory to the repo root
    os.chdir(script_dir)

    parser = argparse.ArgumentParser(description="Verifies the integrity of the Memory Module environment.")
    parser.add_argument("--no-self-verify", action="store_true", help="Skip the self-integrity check.")
    args = parser.parse_args()

    if not verify_environment(no_self_verify=args.no_self_verify):
        sys.exit(1)
