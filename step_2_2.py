from pathlib import Path

from step_2_1 import WORK_DIR  # Import working directory path

# Define a function that calculates the total file size in the given directory
def get_total_filesize(base_dir: Path, pattern: str = "*") -> int:
    total_bytes = 0 # Initialize total byte counter

    # Iterate through all files and subdirectories matching the pattern
    for fullpath in base_dir.glob(pattern):
        # Check if the current path points to a file
        if fullpath.is_file():
            # Add the size of the file (in bytes) to the running tota
            total_bytes += fullpath.stat().st_size
    # Return the total accumulated file size
    return total_bytes

# Run this block only when the script is executed directly
if __name__ == "__main__":
    base_dir = WORK_DIR # Set the target directory to the working directory

    # Calculate total size of all files in the working directory
    filesize = get_total_filesize(base_dir, pattern="*")
    # Print the directory path and the calculated total file size
    print(f"{base_dir.as_posix()=}, {filesize=} bytes")