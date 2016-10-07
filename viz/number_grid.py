import numpy as np
from bokeh.io import show
from bokeh.plotting import figure

n = np.random.rand(100) * 100
n = n.astype(int)
x = np.array(list(range(0, 10)) * 10) + 0.4
y = np.array([[x] * 10 for x in range(0, 10)]).flatten() + 0.4

p = figure(
    x_range=(0, 10), y_range=(0, 10),
    tools='', toolbar_location=None,
    x_axis_type=None, y_axis_type=None,
    outline_line_color=None, background_fill_color='#fdf6e3', border_fill_color=None,
)
p.text(text=n, x=x, y=y)
show(p)
