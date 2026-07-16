import schedule
import time

from update_db import update_database

schedule.every().day.at("10:00").do(update_database)

print("Scheduler Started")

while True:

    schedule.run_pending()

    time.sleep(60)