import os
import sys
import subprocess
import hashlib
import argparse

# The version of the Memory Module environment configuration.
# This will be replaced by the release manager during a release commit.
__version__ = "V0.9.0_7o1Gt3Gq"

CORE_FILE_CHECKSUMS = {
    ".gitignore": "d973552284795a7eade6124b1df32b8920c2791b7a111b23b593eab2154a9186",
    "README.ai": "ffb7c31037494484b401819a8bb3a2549b1750d7f0cfcf0f7fe5ea2d1534c335",
    "README.md": "5bbec21fe7f2829aa8a675526c62e051681279941acd779b349b5d66c43d4ca1",
    "VERSION": "30c99e8b103eacbe6f6d6e1b54b06ca6d5f3164b4f50094334a517ae95ca8fba",
    "json/local_paths.json": "3c46f16ea7deffaaaede72c14843d2bf0d5b427e7e5e5917f85bd4ee692234fb",
    "json/rules/swarm_protocol.json": "2611d24ac52ce620ecf0cd6bb5ca911769052619aacd2e30fb0961ce2623c2f8",
    "py/signatures/generate_salt.py": "6a0db515090f2e6b107f186875fadfae0ce15c7d7187e2998359db80f1b09e3c"
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
        return True # Soft failure for memory modules

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
            print(f"❌ Could not find a 'Release Commit' for version '{my_version}'.")
            return False
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git command failed. Could not search for the release commit.")
        return False

    try:
        show_cmd = ['git', 'show', f'{commit_hash}:{my_path}']
        historical_content = subprocess.check_output(show_cmd)
        historical_checksum = hashlib.sha256(historical_content).hexdigest()
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(f"❌ Git command failed. Could not retrieve historical version of '{my_path}'.")
        return False

    if current_checksum == historical_checksum:
        print(f"✔ Self-integrity check passed for version {my_version}.")
        return True
    else:
        print(f"❌ Self-integrity check failed! Script has been modified since release.")
        return False

def verify_environment(no_self_verify=False):
    print(f"--- verifying Memory Module environment v{__version__} ---")
    all_ok = True
    
    # 1. Remote Configuration
    print("\n[1/4] Checking Remote Configuration...")
    if not check_remote_origin():
        all_ok = False

    # 2. Core Directory Structure
    print("\n[2/4] Checking Core Directory Structure...")
    core_dirs = ["json", "md", "png", "py", "schemas"]
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
    parser = argparse.ArgumentParser(description="Verifies the integrity of the Memory Module environment.")
    parser.add_argument("--no-self-verify", action="store_true", help="Skip the self-integrity check.")
    args = parser.parse_args()

    if not verify_environment(no_self_verify=args.no_self_verify):
        sys.exit(1)
