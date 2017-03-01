from notebook.base.handlers import IPythonHandler
from geopyter.core.vis_gen.visualization_generator import VisualizationGenerator

import json
import pickle

class GeopyterHandler(IPythonHandler):
    """Custom request handler for the /geopyter endpoint

    Manages the creation of visualization code through VisualizationGenerator.
    Requests and responses are sent in JSON format.
    """

    def get(self):
        self.write('GeopyterHandler GET')
    
    def post(self):
        """POST method handler for GeopyterHandler

        Args:
            self.request.body: The body of the HTTP request sent - must be JSON

        Returns:
            HTTP response of JSON:
                js_code: visualization code generated by VisualizationGenerator
        """
        vis_params = json.loads(self.request.body)
        vis_params['data'] = pickle.loads(vis_params['data'])
        vg = VisualizationGenerator(vis_params)

        self.write({'js_code' : vg.create_visulization()})