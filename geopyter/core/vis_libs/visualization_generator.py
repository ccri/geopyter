from ast import literal_eval
from uuid import uuid4 as uuid

from geopyter.core.vis_libs.d3 import d3_generator

# dict of currently supported visualization libraries
# key = visualization library
# val = default create_visualization() function for visualization library
vis_libs = {
    'd3': d3_generator.create_visualization
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
        params['id'] = uu_id[:0] + 'g' + uu_id[1:]
        self.vis_lib, self.vis_type = params.pop('vis').split('.')
        self.data_path = params.pop('data')
        self.vis_params = params

    def create_visulization(self):
        """Sends the visualization request to the specified visualization
            library"""
        # first pass at loading data through python
        self._load_data()
            
        # TODO: better error handling
        if (self.vis_lib not in vis_libs):
            return {'output': 'ERROR: no visualization library found.'}
        
        return vis_libs[self.vis_lib](
            self.data,
            self.vis_type,
            self.vis_params
        )
    
    def _load_data(self):
        f = open(self.data_path, 'r')
        self.data = literal_eval(f.read())