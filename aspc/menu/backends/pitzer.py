# Scraper for Pitzer (McConnell) dining hall.
#
# Originally from https://github.com/sean-adler/5c-dining-api

import feedparser
from collections import defaultdict
from bs4 import BeautifulSoup

class PitzerBackend(object):
    rss = feedparser.parse('http://legacy.cafebonappetit.com/rss/menu/219')
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    menus = { # Menu structure to return
        'mon': {}, # Each day dict contains key value pairs as meal_name, [fooditems]
        'tue': {},
        'wed': {},
        'thu': {},
        'fri': {},
        'sat': {},
        'sun': {}
    }

    def menu(self):
        for entry in self.rss.entries:
            body = BeautifulSoup(entry.summary)
            date = entry.title[:4]
            tm = titles_and_meals = body.findAll(['h3', 'h4'])

            meal_dict = defaultdict(list)

            for m in tm:
                if m.name == 'h3':
                    meal_title = m.text
                elif m.name == 'h4':
                    food = m.text.strip().split(', ')
                    for f in food:
                        station_and_food = f.split('] ')
                        if len(station_and_food) > 1:
                            station = station_and_food[0]
                            food = station_and_food[1]
                            meal_dict[meal_title].append(food.title())
                        else:
                            food = station_and_food[0]
                            meal_dict[meal_title].append(food.title())

            meal_dict = dict(meal_dict)

            self.menus[entry.title[:3].lower()] = {key.lower(): value for key, value in meal_dict.iteritems()}

        return self.menus