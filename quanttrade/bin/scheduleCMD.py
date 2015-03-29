__author__ = 'tyler'
from apscheduler.schedulers.background import BlockingScheduler
from data.YahooFinance import YahooFinance
scheduler = BlockingScheduler()

def downloadHistorical():
    print('schedule start...')
    y = YahooFinance()
    y.downAllStock()
def startSchedule():
    #scheduler.add_job(downloadHistorical, 'cron', day_of_week='0-4', hour='17',id='downloadHistorical')
    scheduler.add_job(downloadHistorical,day_of_week='mon-fri')
    scheduler.start()

#startSchedule()
downloadHistorical()


