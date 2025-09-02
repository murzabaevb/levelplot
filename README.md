# Signal Level Plotter
A flexible Python class for creating signal level visualizations using Matplotlib. This tool is designed for plotting signal levels as thick horizontal lines with centered labels, perfect for visualizing frequency- or time-based signal data across multiple charts.

## Features
- Multiple Chart Support: Create separate subplots for each unique chart identifier
- Clean Line Visualization: Thick horizontal lines instead of bars for clear signal representation
- Centered Labels: Legends positioned exactly in the middle of each signal line
- Overlap Handling: Automatic vertical separation of overlapping signals
- Customizable Titles: User-definable chart titles and axis labels
- Flexible X-Axis Ranges: Auto-ranging or user-specified x-axis limits
- Common X-Axis: All charts share the same x-axis for easy comparison
- Color Coding: Automatic color assignment
- Exclusion Support: Filter out unwanted data entry using the 'exclude' column

## Installation
```bash
# From GitHub
py -m pip install git+https://github.com/murzabaevb/levelplot.git  # on Windows 
python3 -m pip install git+https://github.com/murzabaevb/levelplot.git  # on Unix/macOS

# From local source (for development)
git clone https://github.com/murzabaevb/levelplot.git
cd levelplot
pip install -e .
```

## Quick Start

1. Install the package:
```bash
pip install git+https://github.com/murzabaevb/levelplot.git
```
2. Create your data in a pandas DataFrame with the required columns
3. Import and use:
```python
import pandas as pd
import matplotlib.pyplot as plt
from levelplot import LevelPlot

# Your data here
data = {...}
df = pd.DataFrame(data)

plotter = LevelPlot()
fig, axes = plotter.plot(df)
plt.show()
```


## Usage

### Basic Example

```python
import pandas as pd
import matplotlib.pyplot as plt
from levelplot import LevelPlot


# Create sample data
data = {
    'chart': ['Chart1', 'Chart1', 'Chart2', 'Chart2'],
    'legend': ['Signal_A', 'Signal_B', 'Signal_C', 'Signal_D'],
    'start': [1.0, 3.0, 0.5, 4.0],
    'stop': [4.0, 7.0, 3.0, 8.0],
    'level': [2.0, -1.0, 1.0, -2.0],
    'exclude': [False, False, False, False]
}

df = pd.DataFrame(data)

# Create and use plotter
plotter = LevelPlot()
fig, axes = plotter.plot(df)
plt.show()
```

### Advanced Configuration

```python
# Customize during initialization
plotter = LevelPlot(
    figsize=(14, 9),
    line_width=4.0,
    chart_title_prefix="My Signals - ",
    x_axis_title="Time (ms)",
    y_axis_title="Amplitude (V)",
    x_axis_range=(0, 10)  # Fixed x-axis range
)

# Or customize during plot call (overrides initialization)
fig, axes = plotter.plot(
    df,
    chart_title_prefix="Analysis: ",
    x_axis_title="Time Steps",
    y_axis_title="Signal Level",
    x_axis_range=(2, 8)  # Zoom to specific range
)
```
## Data Format

The class expects a pandas DataFrame with the following columns:

| Column | Description                                                       | Required |
|--------|-------------------------------------------------------------------|----------|
|`chart`| Chart identifier - each unique value creates a separate subplot   |Yes|
|`legend`| Line name - used for labeling and color coding                    |Yes|
|`start`| Line start position on x-axis                                     |Yes|
|`stop`| Line end position on x-axis                                       |Yes|
|`level`| Line level on y-axis (can be positive or negative)                |Yes|
|`exclude`| Boolean flag to exclude specific signals from plotting (optional) |No|

## Configuration Options

### Class Initialization Parameters

```python
LevelPlot(
    figsize=(12, 10),           # Figure size (width, height)
    line_width=3.0,             # Thickness of signal lines
    chart_title_prefix="Signal Levels - ",  # Prefix for chart titles
    x_axis_title="Time",        # X-axis label
    y_axis_title="Level",       # Y-axis label
    x_axis_range=None           # Tuple (x_min, x_max) or None for auto-range
)
```

### Plot Method Parameters

```python
plot(
    df,                         # Input DataFrame
    chart_title_prefix=None,    # Override chart title prefix
    x_axis_title=None,          # Override x-axis title
    y_axis_title=None,          # Override y-axis title
    x_axis_range=None           # Override x-axis range
)
# Returns: (fig, axes) - matplotlib Figure and Axes objects for further customization
```

## Examples

### Multiple Charts with Common X-Axis

```python
# Data spanning multiple charts
data = {
    'chart': ['Voltage', 'Voltage', 'Current', 'Current', 'Power', 'Power'],
    'legend': ['V_Source', 'V_Load', 'I_Source', 'I_Load', 'P_Source', 'P_Load'],
    'start': [1.2, 3.5, 0.5, 4.2, 2.1, 5.0],
    'stop': [4.3, 7.2, 3.5, 8.3, 4.2, 7.5],
    'level': [5.0, 3.0, 2.0, -1.5, 10.0, -8.0]
}

plotter = LevelPlot()
fig, axes = plotter.plot(pd.DataFrame(data))
```

### Custom X-Axis Range

```python
# Focus on specific time interval
plotter.plot(df, x_axis_range=(2, 6))

# Extended view
plotter.plot(df, x_axis_range=(-2, 12))
```

### Custom Styling

```python
# Professional styling for reports
plotter = LevelPlot(
    figsize=(10, 6),
    line_width=4.0,
    chart_title_prefix="Experimental Results - ",
    x_axis_title="Time (seconds)",
    y_axis_title="Voltage (V)",
    x_axis_range=(0, 10)
)
```

## Output Features
- Clean Grid: Dashed grid lines for easy reference
- Zero Reference: Grid line at y=0 (when within range)
- Shared X-Axis: All charts share common x-axis for comparison
- Centered Labels: Text labels positioned exactly on signal lines
- Color Consistency: Same legend values get same colors across charts

## Saving Plots

```python
fig, axes = plotter.plot(df)
plt.savefig('signals.png', dpi=300, bbox_inches='tight')
plt.savefig('signals.pdf', bbox_inches='tight')  # Vector format
```

## Use Cases
- Electrical signal visualization
- Process monitoring timelines
- Resource allocation charts
- Scheduling diagrams
- Any frequency- or time-based level data

## Dependencies
- matplotlib >= 3.9.2

## License

This project is licensed under the GNU General Public License. See the LICENSE.txt file for details.

## Support

For issues or feature requests, please check the code comments for implementation details or create an issue in the project repository.
