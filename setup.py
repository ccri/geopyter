from setuptools import setup, find_packages

setup(name='geopyter',
      version='0.0.1',
      author='Gerard C. Briones',
      author_email='gbriones@ccri.com',
      packages=find_packages(),
      install_requires=[
            'ipython',
            'jupyter',
            'tornado'
      ],
      data_files=[
          ('share/jupyter/nbextensions', [
              'geopyter/geopyter.css',
              'external/d3js/d3.min.js',
              'external/leaflet/leaflet.css',
              'external/leaflet/leaflet.js']),
          ('share/jupyter/nbextensions/images', [
              'external/leaflet/images/layers.png',
              'external/leaflet/images/layers-2x.png',
              'external/leaflet/images/marker-icon.png',
              'external/leaflet/images/marker-icon-2x.png',
              'external/leaflet/images/marker-shadow.png'])
          ]
      )