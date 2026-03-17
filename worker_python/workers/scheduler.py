from apscheduler.schedulers.blocking import BlockingScheduler
from worker_python.main import main

scheduler = BlockingScheduler()

scheduler.add_job(main, "interval", hours=24)

scheduler.start()