# Reddit Img Downloader

Download images from your favourite subreddits with ease

## Getting Started
```
git clone https://github.com/Mario-SO/Reddit_Img_Downloader.git
```
```
cd Reddit_Img_Downloader
```
These ins`ructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will only need the yaml and praw libraries

```
pip install pyyaml && pip install praw
```

### Running

I have prepared a simple initial setup that will guide you through the data the bot needs to work properly.
Go to the configuration folder 

```
cd configuration
```
Then run the initial_setup.py script and fill the data it requires

```
python initial_setup.py
```
Once finished, go to de root directory of the project and run the bot

```
python bot.py
```

### How to improve it

[] Save images in an specific folder for better organization

[] Parse multiple sibreddits at the same time

[] Reorganize the code (I find it a bit messy)

## Authors

* **Mario-SO** - *Initial work* - [Mario-SO](https://github.com/Mario-SO)

See also the list of [contributors](https://github.com/Mario-SO/Reddit_Img_Downloader/graphs/contributors) who participated in this project.
