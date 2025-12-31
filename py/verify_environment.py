import os
import sys
import subprocess
import hashlib
import argparse

# The version of the Memory Module environment configuration.
# This will be replaced by the release manager during a release commit.
__version__ = "V0.8.2_fEbfclvj"

CORE_FILE_CHECKSUMS = {
    "README.ai.json": "e5d40f3abeaf805288b5a2e241c3b2bbe8de1f75bfcfb7bcc2fa1af39478f4d7",
    "README.md": "02d1fba6285a6d6fc03029d5ff5df3b52d2e898191ab571fa11fee330e7b30d8",
    "requirements.txt": "1bcf79ff3bb074ae623f72804b2404863e24ce856e8c4c3762f3102ddfcededd",
    "json/local_paths.json": "3c46f16ea7deffaaaede72c14843d2bf0d5b427e7e5e5917f85bd4ee692234fb",
    "json/rules/swarm_protocol.json": "2611d24ac52ce620ecf0cd6bb5ca911769052619aacd2e30fb0961ce2623c2f8",
    "json/principles/agent_virtues.json": "4fbfd2378a4bb8d778636908ad7ba35ae24a0a499372701d926d4ca951ca7b96",
    "json/configuration/verified_repositories.json": "9dcc60f1261f0dbdfd720dbe4eea551c1072b46aecdf0fcf4cf94c0e6e903b79",
    "json/personality/personality.json": "3f60491bd2a1645091589494da059532188691f6a5076b7752e05ac8c5c7158f",
    "json/philosophy/gem_process.json": "fc210dd5e9b023d2d453568fbf6b13b191d02867d42ec39244da5ddef70d8756",
    "json/schema/wedo_pseudolanguage_schema.json": "cc8aca93bddf8cf4ef277e61b049d5672d5e60a755e551da34018ac9814d46c1",
    "py/verify_environment.py": "1e25cfdb6eaa84bf649b1d7f5eb39fb2d6801525d9200dbee1097699f3c04681",
    "py/signatures/generate_salt.py": "2d002c832e62cb0a261759d2d6f484fbb2ffa18d748b5755d388e3a77bed6d9c",
    "md/wedo/markdown_generation/png_journal.todo.md": "1500212fbf702e2dc3c915a6e3a5cfecb308b4648d58b3d620c41289dd08192c",
    "md/wedo/markdown_generation/boilerplate_report.todo.md": "2d2658d7124fc6d14d0879ab9513313ba8145b5456a53032ab0d38bb3d1870bb",
    "md/wedo/markdown_generation/boilerplate_readme.todo.md": "f71844e116b4d1b5409880b64da8ae4a5b0b7d59161b4d2e81fe464448a7a2d1",
    "md/wedo/markdown_generation/biography.todo.md": "d5706c14ef214d8d7543c2ae7eec719d8ce704e7f49add03fa6424798d5a25a6",
    "md/wedo/github/remote_pull.todo.md": "885fa25641df64a74e634e98146896714133022d5d9d33c14f66c0f13086259a",
    "md/wedo/github/github_audit_repair.todo.md": "1b47487d4fb1f114143a2a7b2392d4b8bbc35c88ab8a978d81231799556b3e38",
    "md/wedo/meta_wedo.todo.md": "6aa9350677476b2ff2e91fe786c7e5dc7d21adf6e496b2944d13e5ac74e5155b",
    "2025/Q4/12/21/md/20251221_Public_Memory_Audit.md": "e3fce5a786a7bbaf05938cc4212917ec7e7d6f5a03aeeb02b094a7268fa8c015",
    "2025/Q4/12/md/Monthly_PNG_Journal_Report_V1.md": "57daba7f9965737fcd01b6d4e721c7d149703d09dccf46a40f65fb5ad9cd3003",
    "2025/Q4/12/md/Monthly_Markdown_Journal_Report_V1.md": "c4c6b22f0f68a600c616041a2217edc3690ceb0f563bafe2b5e8bb656d938092"
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
             # Verify reachability
             print("Checking remote reachability...")
             subprocess.run(['git', 'ls-remote', '--exit-code', 'origin', 'HEAD'], capture_output=True, check=True)
             print("✔ Remote 'origin' is reachable.")
             return True
        else:
            print(f"❌ Git remote 'origin' is set to '{remote_url}'. Expected to contain '{required_path}'.")
            return False
    except subprocess.CalledProcessError:
        print("⚠ Remote verification failed. Ensure origin is configured and reachable.")
        return False 

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
            return True 
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
    
    # 1. Remote Configuration & Reachability
    print("\n[1/4] Checking Remote Configuration & Reachability...")
    if not check_remote_origin():
        all_ok = False

    # 2. Core Directory Structure
    print("\n[2/4] Checking Core Directory Structure...")
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
        if "verify_environment.py" in file_path:
            continue
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
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(script_dir)

    parser = argparse.ArgumentParser(description="Verifies the integrity of the Memory Module environment.")
    parser.add_argument("--no-self-verify", action="store_true", help="Skip the self-integrity check.")
    args = parser.parse_args()

    if not verify_environment(no_self_verify=args.no_self_verify):
        sys.exit(1)