import json

import bs4
import requests

from scraper.models import League, Sport, Bookie


class OlybetTennisDriver(object):
    bookie = Bookie.objects.get(name='Olybet')
    sport = Sport.objects.get(name='Tennis')

    def get_league_listing(self):
        url = 'https://www.olybet.ee/bets/tennis/today'
        # with open('test.txt', 'w') as fp:
        #     fp.write(requests.get(url).text)
        parsed_html = bs4.BeautifulSoup(requests.get(url).text, 'html.parser')
        leagues = []
        for league_html in parsed_html.select('.league'):
            league, created = League.objects.get_or_create(
                sport=self.sport,
                bookie=self.bookie,
                external_id=league_html['onclick'].split('Betting.loadParents(this, ')[1].split(', 1);')[0]
            )
            if created:
                league.name = league_html.select('span')[2].text
                league.save()
            leagues.append(league)

        return leagues

    @staticmethod
    def get_single_league_matches(league_id):
        url_template = 'https://www.olybet.ee/bet/parents/%s/today'
        parsed_html = bs4.BeautifulSoup(json.loads(requests.get(url_template % league_id).text)['data'], 'html.parser')

        #print(parsed_html)
        #print('--------')

    def run(self):
        leagues = self.get_league_listing()
        matches = []
        for league in leagues:
            self.get_single_league_matches(league.external_id)

        return matches
