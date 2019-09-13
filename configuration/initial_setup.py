import yaml
import os

print(
    """

    $$$$$$$\                  $$\       $$\ $$\   $$|
    $$  __$$\                 $$ |      $$ |\__|  $$ |
    $$ |  $$ | $$$$$$\   $$$$$$$ | $$$$$$$ |$$\ $$$$$$|
    $$$$$$$  |$$  __$$\ $$  __$$ |$$  __$$ |$$ |\_$$  _|
    $$  __$$< $$$$$$$$ |$$ /  $$ |$$ /  $$ |$$ |  $$ |
    $$ |  $$ |$$   ____|$$ |  $$ |$$ |  $$ |$$ |  $$ |$$|
    $$ |  $$ |\$$$$$$$\ \$$$$$$$ |\$$$$$$$ |$$ |  \$$$$  |
    \__|  \__| \_______| \_______| \_______|\__|   \____/

    """
)

print("""

    $$$$$$\ $$\      $$\  $$$$$$\        $$$$$$$\             $$|
    \_$$  _|$$$\    $$$ |$$  __$$\       $$  __$$\            $$ |
    $$ |  $$$$\  $$$$ |$$ /  \__|      $$ |  $$ | $$$$$$\ $$$$$$$$|
    $$ |  $$\$$\$$ $$ |$$ |$$$$\       $$$$$$$\ |$$  __$$\\_$$  _|
    $$ |  $$ \$$$  $$ |$$ |\_$$ |      $$  __$$\ $$ /  $$ | $$ |
    $$ |  $$ |\$  /$$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ | $$ |$$|
    $$$$$$\ $$ | \_/ $$ |\$$$$$$  |      $$$$$$$  |\$$$$$$  | \$$$$  |
    \______|\__|     \__| \______/       \_______/  \______/   \____/

    By Mario-SO -> https://github.com/Mario-SO

    """)
print("First you will need to insert your reddit OAuth2 credentials\n")
client_id = input("Copy your personal use script (14 characters): ")
secret_key = input("Copy your secret key (28 characters): ")
user_agent = input("Copy your app name: ")
username = input("Write your reddit username: ")
password = input("Write your reddit password: ")

os.system('clear')

print("Now you are going to setup some custom values for the bot functionality")
os.system('sleep 1')

sub = input("Write the name of the subreddit you want to parse: ")
img_limit = input("Write how many images you want to download (recomend<1000): ")
sort_by = input("Sort by (hot, new, rising): ")

print("==========================================================================================================")
print("|| Now everything is set up, you can run the boy.py script located in the root directory of the project ||")
print("||                                                                                                      ||")
print("|| If you want to change any values, go to the config.yml file that the initial_setup.py script created ||")
print("==========================================================================================================")

filepath = "config.yml"
data_to_dump = {
    "credentials": {
        "client_id": client_id,
        "secre_key": secret_key,
        "user_agent": user_agent,
        "username": username,
        "password": password
    },
    "custom_values": {
        "sub": sub,
        "img_limit": img_limit,
        "sort_by": sort_by
    }
}

def yaml_dump(filepath, data):
    try:
        with open(filepath, "w") as file_descriptor:
            yaml.dump(data, file_descriptor)
    except Exception as e:
        print(e)

yaml_dump("config.yml", data_to_dump)
