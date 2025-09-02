import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class LevelPlot:
    def __init__(self, figsize=(12, 10), line_width=3.0,
                 chart_title_prefix="",
                 x_axis_title="Frequency",
                 y_axis_title="Level",
                 x_axis_range=None):
        self.figsize = figsize
        self.line_width = line_width
        self.chart_title_prefix = chart_title_prefix
        self.x_axis_title = x_axis_title
        self.y_axis_title = y_axis_title
        self.x_axis_range = x_axis_range
        self.color_map = {}
        self.color_palette = list(mcolors.TABLEAU_COLORS.values())

    def _get_color(self, legend):
        if legend not in self.color_map:
            self.color_map[legend] = self.color_palette[len(self.color_map) % len(self.color_palette)]
        return self.color_map[legend]

    def _calculate_vertical_offset(self, chart_data, current_idx):
        current_line = chart_data.iloc[current_idx]
        overlaps = []

        for i, row in chart_data.iterrows():
            if i == current_idx:
                continue
            if not (current_line['stop'] <= row['start'] or current_line['start'] >= row['stop']):
                level_diff = abs(current_line['level'] - row['level'])
                if level_diff < 0.5:
                    overlaps.append(row.get('level_offset', 0))

        if overlaps:
            max_offset = max(overlaps)
            if current_line['level'] >= 0:
                return max_offset + 0.3
            else:
                return max_offset - 0.3
        return 0

    def plot(self, df, chart_title_prefix=None, x_axis_title=None,
             y_axis_title=None, x_axis_range=None):
        chart_title_prefix = chart_title_prefix or self.chart_title_prefix
        x_axis_title = x_axis_title or self.x_axis_title
        y_axis_title = y_axis_title or self.y_axis_title
        x_axis_range = x_axis_range or self.x_axis_range

        if 'exclude' in df.columns:
            df = df[~df['exclude']].copy()

        unique_charts = df['chart'].unique()
        num_charts = len(unique_charts)

        fig, axes = plt.subplots(num_charts, 1, figsize=(self.figsize[0], self.figsize[1]), sharex=True)
        if num_charts == 1:
            axes = [axes]

        if x_axis_range is not None:
            global_x_min, global_x_max = x_axis_range
        else:
            global_x_min = df['start'].min() - 1.0
            global_x_max = df['stop'].max() + 1.0

        for chart_idx, chart_name in enumerate(unique_charts):
            ax = axes[chart_idx]
            chart_data = df[df['chart'] == chart_name].copy()

            chart_data = chart_data.sort_values('start').reset_index(drop=True)
            chart_data['level_offset'] = 0.0

            for i in range(len(chart_data)):
                chart_data.at[i, 'level_offset'] = self._calculate_vertical_offset(chart_data, i)

            for _, row in chart_data.iterrows():
                color = self._get_color(row['legend'])
                y_pos = row['level'] + row['level_offset']

                ax.hlines(y=y_pos, xmin=row['start'], xmax=row['stop'],
                          linewidth=self.line_width, color=color, alpha=0.8)

                mid_point_x = (row['start'] + row['stop']) / 2
                ax.text(mid_point_x, y_pos, row['legend'],
                        ha='center', va='center', fontsize=9, fontweight='bold',
                        bbox=dict(boxstyle="round,pad=0.2", facecolor='white', alpha=0.8,
                                  edgecolor=color, linewidth=0.5))

            ax.set_title(f'{chart_title_prefix}{chart_name}', fontsize=12, fontweight='bold')
            ax.set_ylabel(y_axis_title, fontsize=10)

            all_levels = chart_data['level'] + chart_data['level_offset']
            y_min = all_levels.min() - 0.5
            y_max = all_levels.max() + 0.5

            if y_min < 0 and y_max > 0:
                y_min = min(y_min, -0.5)
                y_max = max(y_max, 0.5)

            ax.set_ylim(y_min, y_max)
            ax.grid(True, alpha=0.3, linestyle='--')

            if chart_idx < num_charts - 1:
                ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)

        axes[-1].set_xlim(global_x_min, global_x_max)
        axes[-1].set_xlabel(x_axis_title, fontsize=12)

        plt.tight_layout()
        plt.subplots_adjust(bottom=0.1)

        return fig, axes
