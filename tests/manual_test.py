import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

# Add the src directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from levelplot import LevelPlot

# Create sample data
data = {
    'chart': ['Voltage', 'Voltage', 'Current', 'Current', 'Power', 'Power'],
    'legend': ['V_Source', 'V_Load', 'I_Source', 'I_Load', 'P_Source', 'P_Load'],
    'start': [1.2, 3.5, 0.5, 4.2, 2.1, 5.0],
    'stop': [4.3, 7.2, 3.5, 8.3, 4.2, 7.5],
    'level': [5.0, 3.0, 2.0, -1.5, 10.0, -8.0],
    'exclude': [False, False, False, False, False, False]
}

df = pd.DataFrame(data)

print("Data range:", df['start'].min(), "to", df['stop'].max())

# Option 1: Auto range (default)
plotter1 = LevelPlot(line_width=4.0, figsize=(12, 8))
fig1, axes1 = plotter1.plot(df)
# plt.savefig('signal_levels_auto_range.png', dpi=300, bbox_inches='tight')
plt.show()

# Option 2: Set range during initialization
plotter2 = LevelPlot(
    line_width=4.0,
    figsize=(12, 8),
    x_axis_range=(0, 10)  # Fixed range from 0 to 10
)
fig2, axes2 = plotter2.plot(df)
# plt.savefig('signal_levels_fixed_range_init.png', dpi=300, bbox_inches='tight')
plt.show()

# Option 3: Set range during plot call (overrides initialization)
plotter3 = LevelPlot(line_width=4.0, figsize=(12, 8))
fig3, axes3 = plotter3.plot(
    df,
    x_axis_range=(2, 6)  # Zoom in on specific region
)
# plt.savefig('signal_levels_zoomed_range.png', dpi=300, bbox_inches='tight')
plt.show()

# Option 4: Set range with negative values
plotter4 = LevelPlot(line_width=4.0, figsize=(12, 8))
fig4, axes4 = plotter4.plot(
    df,
    x_axis_range=(-2, 12)  # Extended range with negative start
)
# plt.savefig('signal_levels_extended_range.png', dpi=300, bbox_inches='tight')
plt.show()