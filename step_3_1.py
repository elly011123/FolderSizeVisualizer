import json
from pathlib import Path

from step_2_1 import OUT_DIR  # Import output directory from step_2_1
from step_2_4 import load_filesize_per_dir # Import the function to load file size data from step_2_4

# Define the output file path for this script as a JSON file in the output directory
OUT_3_1 = OUT_DIR / f"{Path(__file__).stem}.json"

# Function to convert file size data into a plot-friendly structure and save it
def dump_plot_data():
    size_per_path = load_filesize_per_dir() # Load file sizes per directory path

    # Convert absolute paths to just the stem (last part of path) and filter out entries with size > 0
    size_per_stem = {Path(path).stem: size for path, size in size_per_path.items() if size > 0}

    # Create a dictionary with two lists: directory names and their sizes
    plot_data = dict(
        stem=list(size_per_stem.keys()), # List of directory name stems
        size=list(size_per_stem.values()), # List of file sizes
    )

    # Save the plot data to a JSON file
    with open(OUT_3_1, "w", encoding="utf-8") as fp:
        json.dump(plot_data, fp, ensure_ascii=False, indent=2)


# Function to read the plot data from the JSON file
def load_plot_data() -> dict[str, list]:
    if OUT_3_1.is_file(): # Check if the JSON file exists
        with open(OUT_3_1, encoding="utf-8") as fp:
            return json.load(fp) # Return the loaded dictionary
    return {} # Return an empty dictionary if file does not exist

# Execute the dump function only when the script is run directly
if __name__ == "__main__":
    dump_plot_data()