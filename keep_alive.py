import os
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

HEROKU_APP_URL = os.environ["HEROKU_APP_URL"]


def keep_alive():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 11.0; WOW64; rv:99.0) Gecko/20010101 Firefox/99.0"}
    request = requests.get(HEROKU_APP_URL, allow_redirects=True, headers=headers).status_code
    print("(Keeping Dyno Alive) HTTP status codes {} while requesting {}".format(request, HEROKU_APP_URL))


if __name__ == '__main__':
    keep_alive()
    scheduler = BlockingScheduler()
    scheduler.add_job(keep_alive, 'interval', seconds=300)
    try:
        print("Starting Keep Alive Service...")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
