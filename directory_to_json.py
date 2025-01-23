import os
import json

def get_directory_structure(path):
    """
    Recursively builds a directory structure dictionary while excluding hidden files/dirs
    """
    name = os.path.basename(path)
    children = []
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                # Skip hidden files and directories (those starting with .)
                if entry.name.startswith('.'):
                    continue
                
                if entry.is_dir(follow_symlinks=False):
                    children.append(get_directory_structure(entry.path))
                else:
                    children.append({
                        "name": entry.name,
                        "type": "file"
                    })
    except Exception as e:
        print(f"Error scanning {path}: {str(e)}")
        raise
    return {
        "name": name,
        "type": "directory",
        "children": children
    }

if __name__ == "__main__":
    current_dir = os.getcwd()
    structure = get_directory_structure(current_dir)
    
    output_file = "index.json"
    with open(output_file, "w") as json_file:
        json.dump(structure, json_file, indent=4)
    
    print(f"Directory structure saved to {output_file} (hidden files excluded)")
