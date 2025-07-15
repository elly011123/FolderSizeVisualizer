from pathlib import Path

import matplotlib.pyplot as plt # Import pyplot to create and save visual plots

from step_2_1 import OUT_DIR  # Import output directory from step_2_1
from step_3_1 import load_plot_data # Import load_plot_data to retrieve data for plotting

plot_data = load_plot_data() # Call the function to load data needed for plotting

fig, ax = plt.subplots() # Create a figure and axis to prepare for plotting
ax.barh(plot_data["stem"], plot_data["size"]) # Use the axis object to draw a horizontal bar chart

fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png") # Save the chart as a PNG file in the output directory

