import dspy

class GenerateImageTitle(dspy.Signature):
    """Generate a short, descriptive, file-safe title for a screenshot from its original filename."""

    original_filename = dspy.InputField(desc="The original filename of the screenshot, which contains the timestamp.")
    
    descriptive_title = dspy.OutputField(desc="A short, human-readable, file-safe (no special characters) title. Example: 'User-Fixes-Git-Ignore'")
