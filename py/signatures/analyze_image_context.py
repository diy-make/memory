WEDO does the image journal WeDo actually use this? if not, it and other related. py are likely cruft

import dspy

class AnalyzeImageContext(dspy.Signature):
    """Given a title and filename, generate a detailed description and a key takeaway for the screenshot."""

    image_title = dspy.InputField(desc="The descriptive title of the screenshot.")
    original_filename = dspy.InputField(desc="The original filename of the screenshot.")
    
    detailed_description = dspy.OutputField(desc="A one-sentence description of the image's content for use in alt-text and captions.")
    key_takeaway = dspy.OutputField(desc="A single, concise insight or conclusion drawn from the screenshot.")
