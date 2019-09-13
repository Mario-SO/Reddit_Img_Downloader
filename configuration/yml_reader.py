import yaml

filepath = "/Users/marioso/Desktop/reddit_bot/configuration/config.yml"

with open(filepath, "r") as file_descriptor:
    data = yaml.load(file_descriptor, Loader=yaml.FullLoader)

