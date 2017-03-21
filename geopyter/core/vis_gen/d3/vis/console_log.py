import json

def make(data, vis_params):
    data_string = json.dumps(data)

    return "let data = " + data_string + "; console.log(data);"