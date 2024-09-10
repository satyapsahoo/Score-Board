import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.target_score = None
        self.current_score = None
        self.overs = None
        self.wickets = None

    
    # Method to fetch webpage content
    def fetch_content(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.content, "html.parser")
            print("Content fetched successfully.")
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    

    def get_first_innings_score(self):
        try:
            score_div = self.soup.find('div', class_='match-summary')
            # score_elements = score_div.find_all('li', class_='win')
            score_elements = score_div.select('li.win, li.lose')
            # print(score_elements)
            score = score_elements[0].find_all('span')[1].get_text()
            self.current_score = score.split('/')[0]
            self.target_score = self.current_score
            self.wickets = score.split('/')[1]
            self.overs = score_elements[0].find('p').get_text().strip().split(' ')[0].split('/')[0]
        
        except:
            self.target_score = 0
            self.current_score = 0
            self.overs = 0
            self.wickets = 0

    
    def get_second_innings_score(self):
        try:
            score_div = self.soup.find('div', class_='match-summary')
            # score_elements = score_div.find_all('li', class_='win')
            score_elements = score_div.select('li.win, li.lose')
            score = score_elements[1].find_all('span')[1].get_text()
            self.current_score = score.split('/')[0]
            self.wickets = score.split('/')[1]
            self.overs = score_elements[1].find('p').get_text().strip().split(' ')[0].split('/')[0]
        
        except:
            self.current_score = 0
            self.overs = 0
            self.wickets = 0
           