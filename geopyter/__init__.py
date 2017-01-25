from geopyter.jupyter_endpoint.handler import GeopyterHandler

from geopyter.magics import *

def _jupyter_server_extension_paths():
    return [{
        'module': 'geopyter'
    }]

def load_jupyter_server_extension(nb_server_app):
    """
    Called when the extension is loaded.

    Args:
        nb_server_app (NotebookWebApplication): handle to the Notebook webserver instance.
    """
    web_app = nb_server_app.web_app
    host_pattern = '.*$'
    web_app.add_handlers(host_pattern, [
            (r'/geopyter', GeopyterHandler),
        ])

    nb_server_app.log.info('geopyter enabled')