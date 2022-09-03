![CSGO](https://repository-images.githubusercontent.com/20169581/3fbcf480-71c7-11ea-8d8d-5be3b385641d)

<h1 align="center">CSGO Dataset</h1>
<p align="center"><b>A CS:GO HLTV Player Stats Dataset</b></p>

<p align="center"><img src="https://img.shields.io/github/issues/YuvalBogachev/csgo-dataset"> <img src="https://img.shields.io/github/forks/YuvalBogachev/csgo-dataset"> <img src="https://img.shields.io/github/stars/YuvalBogachev/csgo-dataset"> <img src="https://img.shields.io/github/license/YuvalBogachev/csgo-dataset?style=flat"></p>

<p align="center">
  <a href="#about">About</a> •
  <a href="#how-to-get">How To Get</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#dependencies">Dependencies</a> •
  <a href="#contributing">Contirbuting</a> •
  <a href="#license">License</a>
</p>

## About
- I've always enjoyed watching competitive CS:GO (Counter Strike: Global Offensive) and wondered about how rankings were assigned to players.
    - I decided to create a project to collect all the data so a prediction task could be created over the player stats (predict their ranking).
- In this repository is the code required to scrape hltv.org to obtain all the players stats.

## How To Get

```
# Clone the repository
git clone https://github.com/YuvalBogachev/csgo-dataset
```
- After succesfuly cloning the repository, you can do whatever you would like with the files.

## How To Use
- To run the scrapper, issue the command `python csgo_player_scrapper.py`.
    - This script is made to request the web pages at a reasonable pace, so no need to worry about being blocked by hltv.org servers.

## Dependencies
- BeautifulSoup4 (to scrape the web pages)
- tdqm (progress bar)

## Contributing
- The dataset is freely available on Kaggle, so there is no need to actually run the script to obtain the data, the repository is strictly for educational purposes.

## License
- This program is licensed under the GPL V3.
