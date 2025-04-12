import json
import yaml

def read_json(file_name):
    with open(file_name, "r") as file:
        file_content = json.load(file)
    return file_content;


def write_json_to_file(content, dest_file):
    with open(dest_file, "w") as file:
        json.dump(content, file, indent=4)


def write_yml_to_file(content, dest_file):
    with open(dest_file, "w") as file:
        yaml.dump(content, file, indent=4)

def convert_json_to_yml(json_data):
   return yaml.dump(json_data, default_flow_style=False)
