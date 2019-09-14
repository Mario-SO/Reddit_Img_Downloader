import yaml

filepath = "/Users/marioso/Desktop/Reddit_Img_Downloader/configuration/config.yml"

with open(filepath, "r") as file_descriptor:
    data = yaml.load(file_descriptor, Loader=yaml.FullLoader)

