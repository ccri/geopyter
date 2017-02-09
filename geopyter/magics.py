from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic,
    line_cell_magic)
from IPython.display import (HTML, Javascript)

import ast
import os
import requests

@magics_class
class GeopyterMagic(Magics):

    @line_cell_magic
    def geopyter(self, line, cell=None):
        """Direct interface to the /geopyter endpoint to create visualizations

        Parses arguments given to the magic into JSON and sends it to /geopyter.
        A JSON response is returned from /geopyter containing the Javascript
        code necessary to build a visualization for the data provided.

        Args:
            data(data_path): Path to the data file. - REQUIRED
            vis(vis_library.vis_type): Specifies the visualization library and
                type of visualization desired.

        Example:
            %geopyter data(histogram_data.json) vis(d3.histogram)

        Returns:
            A JavaScript visualization powered by the code generated by
            /geopyter. This code is returned in a JSON response and is executed
            through IPython.display.Javascript()
        """

        # append cell to line if there is spillover
        if cell is not None:
            line += ' ' + cell.replace('\n', ' ')

        args = line.strip().split(' ')

        # clean the arguments to be able to pass them as JSON to /geopyter
        cleaned_args = {}
        for arg in args:
            arg = arg.replace(')', '')
            key, value = arg.split('(')
            cleaned_args[key] = value

        # XSRF token setup
        url = 'http://localhost:8888/'
        client = requests.Session()
        # start session to obtain token
        client.get(url)
        # add token to request header
        headers = {'X-XSRFToken': client.cookies['_xsrf']}
        r = client.post(url+'geopyter', json=cleaned_args, headers=headers)

        css = 'http://localhost:8888/nbextensions/geopyter.css'
        
        return Javascript(r.json()['js_code'], css=css)

def load_ipython_extension(ipython):
    ipython.register_magics(GeopyterMagic)