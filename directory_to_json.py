import os
import json

def get_directory_structure(path):
    """
    Recursively builds a directory structure dictionary starting from the given path.
    """
    name = os.path.basename(path)
    children = []
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir(follow_symlinks=False):
                    # Process directory
                    children.append(get_directory_structure(entry.path))
                else:
                    # Process file
                    children.append({
                        "name": entry.name,
                        "type": "file"
                    })
    except PermissionError:
        pass  # Handle permission errors silently
    return {
        "name": name,
        "type": "directory",
        "children": children
    }

if __name__ == "__main__":
    current_dir = os.getcwd()
    structure = get_directory_structure(current_dir)
    
    output_file = "directory_structure.json"
    with open(output_file, "w") as json_file:
        json.dump(structure, json_file, indent=4)
    
    print(f"Current directory structure saved to {output_file}")
