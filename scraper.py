# import os
import requests
import pprint
# from bs4 import BeautifulSoup
# from datetime import datetime, timedelta
# from slacker import Slacker

# checks our rss feed for any story not in the high-school-fooball subdirectory,
# containing one of the city names defined below, that's published in the last hour, and then publishes
# those stories to the #feed-newsletter-<<cityname>> slack channel.

last_days = [20200131, 20200228, 20200331, 20200430, 20200531, 20200630]

def perform_scrape():



    request = requests.get('https://covidtracking.com/api/states/daily')
    data = request.json()
    pprint.pprint(data)
    filterList = ['TX']

    texas_data = list(filter(lambda d: d['state'] in filterList, data))

    current_date = str(texas_data[0]["date"])
    month_string = current_date[4:6]
    current_month = int(month_string)

    for i, d in enumerate(texas_data):
      if i < len(texas_data) - 1:
        try: 
          d["positive_count"] = d["positive"] - texas_data[i + 1]["positive"]
        except TypeError:
          d["positive_count"] = d["positive"]
        try: 
          d["total_count"] = d["total"] - texas_data[i+1]["total"]
        except TypeError: 
          d["total_count"] = d["total"]
        try: 
          d["death_count"] = d["death"] - texas_data[i+1]["death"]
        except TypeError:
          d["death_count"] = d["death"]

      else:
        d["positive_count"] = d["positive"]
        d["total_count"] = d["total"]
        d["death_count"] = d["death"]

    if texas_data[0]["date"] < last_days[current_month - 1]:
      current_day = texas_data[0]["date"]

      for x in range(current_day + 1, last_days[current_month - 1] + 1):
        preview_day = {
          "date": x,
          "state": "TX",
          "positive": 0,
          "negative": 0,
          "pending": 0,
          "confirmed_count": 0,
          "total_count": 0,
          "death_count": 0,
          "death": 0,
          "total": 0,
          "dateChecked": texas_data[0]["dateChecked"],
        }

        texas_data.insert(0, preview_day)


    pprint.pprint(texas_data)

    return texas_data