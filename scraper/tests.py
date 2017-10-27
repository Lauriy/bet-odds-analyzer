import os

import requests_mock
from django.conf import settings
from django.test import TestCase

from scraper.drivers.olybet_tennis import OlybetTennisDriver


class ScraperTests(TestCase):
    fixtures = [
        'sport.json',
        'bookie.json'
    ]

    @requests_mock.mock()
    def test_olybet_tennis_driver(self, mock):
        listing = open(os.path.join(settings.BASE_DIR, 'scraper/test_data/tennis/olybet/league_listing.html'))
        league_15532 = open(os.path.join(settings.BASE_DIR, 'scraper/test_data/tennis/olybet/15532.json'))
        league_17795 = open(os.path.join(settings.BASE_DIR, 'scraper/test_data/tennis/olybet/17795.json'))
        league_20231 = open(os.path.join(settings.BASE_DIR, 'scraper/test_data/tennis/olybet/20231.json'))

        mock.get('https://www.olybet.ee/bets/tennis/today', text=listing.read())
        mock.get('https://www.olybet.ee/bet/parents/15532/today', text=league_15532.read())
        mock.get('https://www.olybet.ee/bet/parents/17795/today', text=league_17795.read())
        mock.get('https://www.olybet.ee/bet/parents/20231/today', text=league_20231.read())

        listing.close()
        league_15532.close()
        league_17795.close()
        league_20231.close()

        driver = OlybetTennisDriver()
        driver.run()
