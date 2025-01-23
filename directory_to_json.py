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
                    children.append(get_directory_structure(entry.path))
                else:
                    children.append({
                        "name": entry.name,
                        "type": "file"
                    })
    except Exception as e:
        print(f"Error scanning {path}: {str(e)}")
        raise  # Re-raise the exception to see it in GitHub logs
    return {
        "name": name,
        "type": "directory",
        "children": children
    }

if __name__ == "__main__":
    try:
        current_dir = os.getcwd()
        print(f"Scanning directory: {current_dir}")  # Debug output
        
        structure = get_directory_structure(current_dir)
        
        output_file = "index.json"
        with open(output_file, "w") as json_file:
            json.dump(structure, json_file, indent=4)
            
        print(f"Successfully generated {output_file}")
        print("File contents preview:", json.dumps(structure, indent=4)[:500] + "...")  # Truncated preview

    except Exception as e:
        print(f"Critical error: {str(e)}")
        raise  # Ensure failure is visible in GitHub Actions
