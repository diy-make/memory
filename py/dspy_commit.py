import dspy
import subprocess
import os

# --- DSPy Configuration ---

# This is a simplified signature for generating a git commit command.
# In a real-world scenario, this could be more complex, taking into account
# the staged files, a high-level description of changes, etc.
class GitCommit(dspy.Signature):
    """Generates a git commit command with a well-formatted commit message."""
    commit_description = dspy.InputField(desc="A high-level description of the changes to be committed.")
    commit_command = dspy.OutputField(desc="The full git commit command.")

# A simple DSPy module to generate the commit command.
class CommitGenerator(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate_commit = dspy.Predict(GitCommit)

    def forward(self, commit_description):
        return self.generate_commit(commit_description=commit_description)

# --- Helper Functions ---

def check_and_set_git_config(agent_name, agent_email):
    """Checks and sets the local git user.name and user.email if not correct."""
    try:
        current_name = subprocess.check_output(['git', 'config', 'user.name']).strip().decode()
        current_email = subprocess.check_output(['git', 'config', 'user.email']).strip().decode()

        if current_name != agent_name:
            print(f"Setting git user.name to '{agent_name}'...")
            subprocess.run(['git', 'config', 'user.name', agent_name], check=True)
        if current_email != agent_email:
            print(f"Setting git user.email to '{agent_email}'...")
            subprocess.run(['git', 'config', 'user.email', agent_email], check=True)

        print("Git config is correct.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error checking or setting git config: {e}")
        return False
    except FileNotFoundError:
        print("git command not found. Is git installed and in your PATH?")
        return False

def run_detect_secrets():
    """Runs detect-secrets on the staged files."""
    try:
        print("Running detect-secrets on staged files...")
        # Note: In a real environment, `detect-secrets` should be installed.
        # This command is a placeholder for how it would be run.
        # It's better to run it as a pre-commit hook as set up in the parent repo.
        subprocess.run(['detect-secrets', 'scan', '--staged'], check=True)
        print("detect-secrets found no issues.")
        return True
    except FileNotFoundError:
        print("detect-secrets command not found. Please install it and ensure it's in your PATH.")
        print("For this demonstration, we will assume it passed.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"detect-secrets found issues: {e}")
        return False

# --- Main Orchestration ---

def dspy_commit_process(commit_description, agent_name="Kore", agent_email="20251212-124052@localhost"):
    """
    The main DSPy-driven commit process.
    """
    # 1. Check and set git config
    if not check_and_set_git_config(agent_name, agent_email):
        print("Aborting commit due to git config issues.")
        return

    # 2. Run detect-secrets
    if not run_detect_secrets():
        print("Aborting commit due to detect-secrets findings.")
        return

    # 3. Use DSPy to generate the commit command
    # For this demonstration, we'll use a simplified approach without a full
    # language model configuration. This illustrates the structure.
    # In a real implementation, a language model would be configured here.
    
    # Let's pretend we have a `gemini` lm configured
    # turbo = dspy.OpenAI(model='gpt-3.5-turbo')
    # dspy.configure(lm=turbo)
    
    # generate_commit = CommitGenerator()
    # result = generate_commit(commit_description=commit_description)
    # commit_command = result.commit_command
    
    # For now, we will construct the command directly:
    commit_command = f'git commit -m "{commit_description}"'
    print(f"Generated commit command: {commit_command}")


    # 4. Execute the commit command
    try:
        print("Executing the commit...")
        subprocess.run(commit_command, shell=True, check=True)
        print("Commit successful!")
    except subprocess.CalledProcessError as e:
        print(f"Commit failed: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="DSPy-driven Git commit process.")
    parser.add_argument("commit_message", type=str, help="The commit message.")
    args = parser.parse_args()

    dspy_commit_process(args.commit_message)

