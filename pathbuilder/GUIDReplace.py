import uuid
import os

def insert_guid(filename):
    """Insert a new GUID in every empty value of the "id" key."""
    
    # Read the file
    with open(filename, 'r') as file:
        content = file.read()

    # Define the target pattern
    target_pattern = '"id": ""'

    # While the pattern still exists in the content, keep replacing
    while target_pattern in content:
        replacement = '"id": "{}"'.format(str(uuid.uuid4()))
        content = content.replace(target_pattern, replacement, 1) # Only replace the first occurrence
    
    # Write the updated content back to the file
    with open(filename, 'w') as file:
        file.write(content)

# Determine the path of the current Python file
current_path = os.path.dirname(os.path.abspath(__file__))
list_of_marks = {
    #"Aberrant",
    #"Detection",
    #"Finding",
    #"Handling",
    #"Healing",
    #"Hospitality",
    #"Making",
    #"Passage",
    #"Scribing",
    #"Sentinel",
    #"Shadow",
    #"Storm",
    #"Warding"
    "Least"
}

# Create the full path to the target file
for mark in list_of_marks:
    filename = os.path.join(current_path, mark+".json")
    insert_guid(filename)
