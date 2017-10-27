from django.core.management.base import BaseCommand

from scraper.drivers.olybet_tennis import OlybetTennisDriver


class Command(BaseCommand):
    help = 'Runs all scrape drivers and stores results'

    def handle(self, *args, **options):
        driver1 = OlybetTennisDriver()
        driver1.run()
