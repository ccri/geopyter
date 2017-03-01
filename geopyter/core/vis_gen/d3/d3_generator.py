from geopyter.core.vis_gen.d3.vis import *

# dict of currently supported visualization types for D3js
# key = visualization type
# val = default make() function for visualization type
vis_types = {
    'console_log': console_log.make,
    'histogram': histogram.make,
    'table': table.make,
    'timeseries': timeseries.make
}

def create_visualization(data, vis_type, vis_params):
    return vis_types[vis_type](data, vis_params)