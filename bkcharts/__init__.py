from __future__ import absolute_import


# defaults and constants
DEFAULT_PALETTE = ["#f22c40", "#5ab738", "#407ee7", "#df5320", "#00ad9c", "#c33ff3"]

# main components
from .chart import Chart, defaults

# operations and attributes for users to input into Charts
from .attributes import color, marker, cat
from .operations import stack, blend
from .stats import bins

# builders
from .builders.line_builder import Line
from .builders.histogram_builder import Histogram
from .builders.bar_builder import Bar
from .builders.scatter_builder import Scatter
from .builders.boxplot_builder import BoxPlot
from .builders.step_builder import Step
from .builders.timeseries_builder import TimeSeries
from .builders.dot_builder import Dot
from .builders.area_builder import Area
from .builders.horizon_builder import Horizon
from .builders.heatmap_builder import HeatMap
from .builders.donut_builder import Donut
from .builders.chord_builder import Chord

# easy access to required bokeh components
from bokeh.models import ColumnDataSource; ColumnDataSource
from bokeh.io import curdoc, output_file, output_notebook, reset_output, save, show
from bokeh.layouts import gridplot

# Silence pyflakes
(curdoc, output_file, output_notebook, reset_output, save, show, gridplot)
