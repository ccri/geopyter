from geopyter.core.vis_libs.d3.vis import histogram, table, timeseries

# dict of currently supported visualization types for D3js
# key = visualization type
# val = default make() function for visualization type
vis_types = {
    'histogram': histogram.make,
    'table': table.make,
    'timeseries': timeseries.make
}

def create_visualization(data_path, vis_type, vis_params):
    return vis_types[vis_type](data_path, vis_params)