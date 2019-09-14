import yaml

filepath = "/Path/to/your/config/file/config.yml"

with open(filepath, "r") as file_descriptor:
    data = yaml.load(file_descriptor, Loader=yaml.FullLoader)

