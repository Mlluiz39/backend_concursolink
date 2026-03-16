from apscheduler.schedulers.blocking import BlockingScheduler
from main import main

scheduler = BlockingScheduler()

scheduler.add_job(main, "interval", hours=24)

scheduler.start()