from pathlib import Path

# Define the working directory as the directory of the current script
WORK_DIR = Path(__file__).parent

# Define the output directory inside the working directory3
OUT_DIR = WORK_DIR / "output"

# If executed directly, create the output directory
if __name__ == "__main__":
    OUT_DIR.mkdir(exist_ok=True)

