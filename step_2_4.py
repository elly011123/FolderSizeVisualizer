import json
from pathlib import Path

from step_2_1 import OUT_DIR  # Import shared output directory path from step_2_1

# Import functions to get total file size and directory names
from step_2_2 import get_total_filesize 
from step_2_3 import load_dirnames

# Define the output JSON file path using the current filename
OUT_2_4 = OUT_DIR / f"{Path(__file__).stem}.json"

# Define a mapping of directory path → total file size, and write it to a JSON file
def dump_filesize_from_dirnames():
    dirs = load_dirnames() # Load list of directory paths from previous step
    result = {} # Dictionary to store path → total size

    for path_str in dirs:
        path = Path(path_str) # Convert string path to Path object
        filesize = get_total_filesize(path, pattern="**/*") # Recursively get total size of files in directory
        result[path.as_posix()] = filesize # Save result using POSIX-style path as key

    # Write the result dictionary to a JSON file with UTF-8 encoding and indentation
    with open(OUT_2_4, "w", encoding="utf-8") as fp:
        json.dump(result, fp, ensure_ascii=False, indent=2)

# Read the JSON file and return the mapping of directory → file size
def load_filesize_per_dir() -> dict[str, int]:
    if OUT_2_4.is_file(): # Check if the JSON file exists
        with open(OUT_2_4, encoding="utf-8") as fp:
            return json.load(fp) # Load and return JSON data as a dictionary
    return {} # Return empty dictionary if the file is missing

# If run as a script, execute the dump function
if __name__ == "__main__":
    dump_filesize_from_dirnames()

