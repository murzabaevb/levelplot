import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

# Add the src directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from levelplot import LevelPlot


def test_basic_functionality():
    """Test basic functionality with simple data"""
    print("Testing basic functionality...")

    # Create test data
    data = {
        'chart': ['TestChart', 'TestChart'],
        'legend': ['Signal_1', 'Signal_2'],
        'start': [1.0, 3.0],
        'stop': [4.0, 6.0],
        'level': [2.0, 1.0],
        'exclude': [False, False]
    }

    df = pd.DataFrame(data)

    # Create plotter and plot
    plotter = LevelPlot()
    fig, axes = plotter.plot(df)

    plt.savefig('test_basic.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Basic test completed - check test_basic.png")


def test_multiple_charts():
    """Test multiple charts with common x-axis"""
    print("Testing multiple charts...")

    data = {
        'chart': ['Voltage', 'Voltage', 'Current', 'Current', 'Power', 'Power'],
        'legend': ['V_Source', 'V_Load', 'I_Source', 'I_Load', 'P_Source', 'P_Load'],
        'start': [1.2, 3.5, 0.5, 4.2, 2.1, 5.0],
        'stop': [4.3, 7.2, 3.5, 8.3, 4.2, 7.5],
        'level': [5.0, 3.0, 2.0, -1.5, 10.0, -8.0],
        'exclude': [False, False, False, False, False, False]
    }

    df = pd.DataFrame(data)

    plotter = LevelPlot(figsize=(10, 8), line_width=4.0)
    fig, axes = plotter.plot(df)

    plt.savefig('test_multiple_charts.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Multiple charts test completed - check test_multiple_charts.png")


def test_custom_titles():
    """Test custom title functionality"""
    print("Testing custom titles...")

    data = {
        'chart': ['CustomChart'],
        'legend': ['TestSignal'],
        'start': [1.0],
        'stop': [5.0],
        'level': [2.0]
    }

    df = pd.DataFrame(data)

    plotter = LevelPlot(
        chart_title_prefix="My Analysis - ",
        x_axis_title="Time (seconds)",
        y_axis_title="Amplitude (V)"
    )

    fig, axes = plotter.plot(df)
    plt.savefig('test_custom_titles.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Custom titles test completed")


def test_x_axis_range():
    """Test custom x-axis range"""
    print("Testing x-axis range...")

    data = {
        'chart': ['RangeTest'],
        'legend': ['RangeSignal'],
        'start': [2.0],
        'stop': [8.0],
        'level': [3.0]
    }

    df = pd.DataFrame(data)

    # Test zoomed-in range
    plotter = LevelPlot()
    fig, axes = plotter.plot(df, x_axis_range=(3, 7))
    plt.savefig('test_zoomed_range.png', dpi=150, bbox_inches='tight')
    plt.close()

    # Test extended range
    fig, axes = plotter.plot(df, x_axis_range=(0, 15))
    plt.savefig('test_extended_range.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ X-axis range tests completed")


def test_negative_levels():
    """Test negative signal levels"""
    print("Testing negative levels...")

    data = {
        'chart': ['NegativeTest'],
        'legend': ['NegativeSignal'],
        'start': [1.0],
        'stop': [5.0],
        'level': [-3.0]
    }

    df = pd.DataFrame(data)

    plotter = LevelPlot()
    fig, axes = plotter.plot(df)
    plt.savefig('test_negative_levels.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Negative levels test completed")


def test_exclusion():
    """Test exclusion functionality"""
    print("Testing exclusion...")

    data = {
        'chart': ['ExclusionTest', 'ExclusionTest'],
        'legend': ['KeepMe', 'ExcludeMe'],
        'start': [1.0, 3.0],
        'stop': [4.0, 6.0],
        'level': [2.0, 1.0],
        'exclude': [False, True]
    }

    df = pd.DataFrame(data)

    plotter = LevelPlot()
    fig, axes = plotter.plot(df)
    plt.savefig('test_exclusion.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Exclusion test completed")


def test_overlapping_signals():
    """Test overlapping signal handling"""
    print("Testing overlapping signals...")

    data = {
        'chart': ['OverlapTest', 'OverlapTest', 'OverlapTest'],
        'legend': ['Signal_A', 'Signal_B', 'Signal_C'],
        'start': [1.0, 2.0, 3.0],
        'stop': [5.0, 4.0, 6.0],
        'level': [2.0, 2.0, 2.0],  # Same level to force overlap
        'exclude': [False, False, False]
    }

    df = pd.DataFrame(data)

    plotter = LevelPlot()
    fig, axes = plotter.plot(df)
    plt.savefig('test_overlapping.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("✓ Overlapping signals test completed")


def run_all_tests():
    """Run all test functions"""
    print("Starting SignalLevelPlotter tests...\n")

    tests = [
        test_basic_functionality,
        test_multiple_charts,
        test_custom_titles,
        test_x_axis_range,
        test_negative_levels,
        test_exclusion,
        test_overlapping_signals
    ]

    for test in tests:
        try:
            test()
            print(f"✓ {test.__name__} passed\n")
        except Exception as e:
            print(f"✗ {test.__name__} failed: {e}\n")

    print("All tests completed! Check the generated PNG files.")


if __name__ == "__main__":
    run_all_tests()