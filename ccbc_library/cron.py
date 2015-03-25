from django_cron import CronJobBase, Schedule
from ccbclib import tasks

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 1 minute

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'ccbclib.weeklycheck'    # a unique code

    def do(self):
        # do your thing here
        print("!!!")
        tasks.SendTestMail()
        