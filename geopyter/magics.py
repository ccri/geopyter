from IPython.core.magic import (Magics, magics_class, line_magic)
from IPython.display import (HTML, Javascript)

# from geopyter.core.data_prep import load_data

import argparse
import csv
import json
import os
import pickle
import requests

@magics_class
class GeopyterMagic(Magics):

    @line_magic
    def geopyter(self, line=None):
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

        parser = argparse.ArgumentParser()
        parser.add_argument('--data',
                            metavar='data',
                            type=str,
                            nargs='?',
                            default='',
                            help='path to the data file')
        parser.add_argument('--vis',
                            metavar='vis',
                            type=str,
                            nargs='?',
                            default=None,
                            help='type of visualization')
        parser.add_argument('--x',
                            metavar='x',
                            type=str,
                            nargs='?',
                            default=None,
                            help='value to treat as x')
        parser.add_argument('--y',
                            metavar='y',
                            type=str,
                            nargs='?',
                            default=None,
                            help='value to treat as y')

        # parse the arguments passed through line
        raw_args = line.split(' ')
        if (raw_args[0] == '' or '-h' in raw_args or '--help' in raw_args):
            parser.print_help()
            return
        args = parser.parse_args(raw_args)

        data_type, data_key = args.data.split(':')
        loaded_data = self._load_data(data_key, data_type)
        args.data = pickle.dumps(loaded_data)

        # XSRF token setup
        url = 'http://localhost:8888/'
        client = requests.Session()
        # start session to obtain token
        client.get(url)
        # add token to request header
        headers = {'X-XSRFToken': client.cookies['_xsrf']}
        r = client.post(url+'geopyter', json=vars(args), headers=headers)

        css = [
            'http://localhost:8888/nbextensions/geopyter.css',
            'http://localhost:8888/nbextensions/leaflet.css'
        ]
        
        # print r.json()['js_code']
        return Javascript(r.json()['js_code'], css=css)

    @line_magic
    def test_data_loading(self, line=None):
        parser = argparse.ArgumentParser()
        parser.add_argument('--data',
                            metavar='data',
                            type=str,
                            nargs='?',
                            default='',
                            help='data path')

        # parse the arguments passed through line
        raw_args = line.split(' ')
        if (raw_args[0] == '' or '-h' in raw_args or '--help' in raw_args):
            parser.print_help()
            return
        args = parser.parse_args(raw_args)

        data_type, data_key = args.data.split(':')
        loaded_data = self._load_data(data_key, data_type)

    def _load_data(self, data_key, data_type):
        data_types = {
            'file': self.__load_file,
            'var': self.__load_var
        }

        return data_types[data_type](data_key)

    def __load_file(self, data_key):
        f = open(data_key, 'r')
        fn, ext = os.path.splitext(data_key)
        ext = ext.lower()

        if (ext == '.csv'):
            return list(csv.DictReader(f.read().splitlines(), delimiter=','))
        elif (ext == '.tsv'):
            return list(csv.DictReader(f.read().splitlines(), delimiter='\t'))
        elif (ext == '.json'):
            return json.loads(f.read())

    def __load_var(self, data_key):
        return self.shell.user_ns[data_key]

def load_ipython_extension(ipython):
    ipython.register_magics(GeopyterMagic)