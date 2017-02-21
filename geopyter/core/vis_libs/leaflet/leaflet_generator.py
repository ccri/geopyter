from geopyter.core.vis_libs.leaflet.vis import leaflet_map

# dict of currently supported visualization types for leaflet
# key = visualization type
# val = default make() function for visualization type
vis_types = {
    'map': leaflet_map.make
}

def create_visualization(data_path, vis_type, vis_params):
    return vis_types[vis_type](data_path, vis_params)