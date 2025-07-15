import json
from pathlib import Path

from step_2_1 import OUT_DIR  # Import the output directory path 

# Define the full path of the output JSON file based on the filename of this script
OUT_2_3 = OUT_DIR / f"{Path(__file__).stem}.json"

# Write a list of subdirectory paths from a base directory to the JSON file
def dump_dirnames(base_dir: Path) -> None:
    dirs = [] # Initialize an empty list to store directory paths

    # Iterate through all items in the base directory
    for path in base_dir.iterdir():
        # Check if the item is a directory
        if path.is_dir():
            # Append the directory path as a string (POSIX format) to the list
            dirs.append(path.as_posix())
    # Sort the list of directories alphabetically
    dirs_sorted = sorted(dirs)

    # Write the sorted list to a JSON file in UTF-8 encoding
    with open(OUT_2_3, "w", encoding="utf-8") as fp:
        json.dump(dirs_sorted, fp, ensure_ascii=False, indent=2)


# Load the list of directory paths from the JSON file
def load_dirnames() -> list[str]:
    # Check if the JSON file exists
    if OUT_2_3.is_file():
        # Read the file and return its contents as a Python list
        with open(OUT_2_3, encoding="utf-8") as fp:
            return json.load(fp)
    return [] # Return an empty list if the file doesn't exist


# If this script is executed directly, dump directory names from the user's home directory
if __name__ == "__main__":
    dump_dirnames(Path.home())

