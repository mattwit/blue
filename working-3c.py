from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, curdoc
from functools import partial
from tornado.ioloop import IOLoop
import zmq.asyncio
from bokeh.models.formatters import DatetimeTickFormatter


doc = curdoc()

context = zmq.asyncio.Context.instance()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:1234")
socket.setsockopt(zmq.SUBSCRIBE, b"")

def update(new_data):
    source.stream(new_data, rollover=50)

async def loop():
    while True:
        new_data = await socket.recv_pyobj()
        doc.add_next_tick_callback(partial(update, new_data))

source = ColumnDataSource(data=dict(x=[0], y=[0]))

plot = figure(height=300, x_axis_type='datetime', plot_width=1500, y_range=(0,1600))

plot.yaxis.axis_label = "frame length"
plot.xaxis.axis_label = 'time'


plot.xaxis.formatter = DatetimeTickFormatter(hours="%H:%M:%S", seconds="%H:%M:%S", microseconds="%H:%M:%S:%s", milliseconds="%H:%M:%S:%s")

plot.line(x='x', y='y', source=source)

doc.add_root(plot)
IOLoop.current().spawn_callback(loop)