from bs4 import BeautifulSoup
from requests import get
from time import sleep
from tqdm import tqdm

''' Extract a link from raw player HTML '''
def get_player_link(player_raw_html):
    _local_player_soup = BeautifulSoup(str(player_raw_html), 'html.parser')
    player_link = _local_player_soup.find('a')['href']
    return player_link


''' Get all relevant stats from player page '''
def get_stats_from_page(player_page_link):
    stats = []
    page = get(player_page_link)
    # Sleep to avoid getting banned from accessing the website
    sleep(0.1)
    stats_soup = BeautifulSoup(page.content, 'html.parser')

    # Get player name
    name_tag = stats_soup.find('h1', class_='summaryNickname text-ellipsis')
    stats.append(name_tag.get_text())

    # Get other stats
    stat_boxes = stats_soup.find_all('div', class_='stats-row')
    for stat_html in stat_boxes:
        stat_html_soup = BeautifulSoup(str(stat_html), 'html.parser')
        stat = stat_html_soup.find_all('span')[-1].get_text()
        # Headshot is given with a percentage sign, remove it
        if stat[-1] == '%':
            stat = stat[:-1]
        stats.append(stat)
    other_stats = stats_soup.find_all('div', class_='summaryStatBreakdownDataValue')
    # Remove the percentage sign from the KAST score
    kast = other_stats[2].get_text()[:-1]
    stats.insert(-1, kast)
    impact = other_stats[3].get_text()
    stats.insert(-1, impact)
    
    return stats

def main():
    # The base url we will use for all navigation purposes
    base_url = "https://www.hltv.org"
    # Get the full players ranking page
    players_page = get(base_url + "/stats/players?startDate=all")
    players_soup = BeautifulSoup(players_page.content, 'html.parser')
    # Locate the player table in the page and extract all players
    players_soup_table = players_soup.find('tbody')
    players_list = players_soup_table.find_all('td', class_='playerCol')
    
    players_link_list = []
    # Get links to the players pages from the table
    for player_raw_html in players_list:
        players_link_list.append(base_url + get_player_link(player_raw_html))

    # Write player stats to CSV (use utf-8 for full utf character support)
    with open('csgo_player_stats.csv', 'w', encoding='utf-8') as file:
        file.write("Name, Total Kills, Headshot Percentage, Total Deaths, Kill/Death Ratio," 
        "Damage Per Round, Grenade Damage Per Round, Maps Played, Rounds Played, Kills Per Round, Assists Per Round,"
        "Deaths Per Round, Saved By Teamates Per Round, Saved Teamates Per Round, KAST, Impact, Rating 2.0\n")
        for player_link in tqdm(players_link_list):
            player_stats = get_stats_from_page(player_link)
            file.write(",".join(player_stats) + '\n')


if __name__ == "__main__":
    main()