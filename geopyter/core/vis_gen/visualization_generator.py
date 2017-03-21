from ast import literal_eval
from uuid import uuid4 as uuid

from geopyter.core.vis_gen.d3 import d3_generator
from geopyter.core.vis_gen.leaflet import leaflet_generator

# dict of currently supported visualization libraries
# key = visualization library
# val = default create_visualization() function for visualization library
vis_libs = {
    'd3': d3_generator.create_visualization,
    'leaflet': leaflet_generator.create_visualization
}

class VisualizationGenerator:
    """Base visualization generator - visualizations are proxied through this

    A UUID is generated for each visualization and the parameters provided to
    this class are sent along to the specified generators for the supported
    visualization libraries.

    Attributes:
        vis_lib: The requested visualization library.
        data_path: The path to the data file to be visualized.
        vis_params: The remaining parameters for the requested
            visualization type.
    """

    def __init__(self, params):
        """Inits VisualizationGenerator with the params sent in the request"""

        # generate a unique id for the visualization element
        uu_id = str(uuid())

        # make first character of UUID alphabetic,
        # html ids cannot start with a number
        params['id'] = uu_id[:0] + 'g' + uu_id[1:]

        # check for default %geopyter call
        if (not params['vis']):
            params['vis'] = 'd3:table'
        self.vis_lib, self.vis_type = params.pop('vis').split(':')
        self.data = params.pop('data')
        self.vis_params = params

    def create_visulization(self):
        """Sends the visualization request to the specified visualization
            library"""

            
        # TODO: better error handling
        if (self.vis_lib not in vis_libs):
            return {'output': 'ERROR: no visualization library found.'}
        
        return vis_libs[self.vis_lib](
            self.data,
            self.vis_type,
            self.vis_params
        )