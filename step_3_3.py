from pathlib import Path
import matplotlib.pyplot as plt # Import pyplot to create and save visual plots
import numpy as np # Import numpy to perform numerical operations
from step_2_1 import OUT_DIR # Import output directory from step_2_1
from step_3_1 import load_plot_data # Import load_plot_data to retrieve data for plotting


plot_data = load_plot_data() # Call the function to load data needed for plotting
log_size = np.log(plot_data["size"]) # Convert raw sizes to log-scale values

fig, ax = plt.subplots(figsize=(16, 9), dpi=100) # Create a large figure and axis with HD resolution
ax.barh(plot_data["stem"], log_size) # Draw a horizontal bar chart
ax.grid(True, axis="x") # Display grid lines only on the x-axis
ax.tick_params(labelbottom=False, length=0, labelsize=20) # Hide bottom ticks and enlarge labels


fig.set_layout_engine("tight") # Enable tight layout to reduce empty margins
fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png") # Save the plot as a PNG file