import csv
import json
import os

def load_data(data, type):
    # code here

def load_file(data_path):
    f = open(data_path, 'r')
    fn, ext = os.path.splitext(data_path)
    ext = ext.lower()

    if (ext == '.csv'):
        return csv.DictReader(f.read().splitlines(), delimiter=',')
    elif (ext == '.tsv')
        return csv.DictReader(f.read().splitlines(), delimiter='\t')
    elif (ext == '.json')
        return json.loads(f.read())