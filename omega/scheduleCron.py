from crontab import CronTab

cron = CronTab(user=True)
print("HI",cron)
job = cron.new(command='python views.py')
job.minute.every(1)

cron.write()
print(job.enable())