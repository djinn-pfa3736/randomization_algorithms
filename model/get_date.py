# Package
import datetime
import logging

# Logging setting
formatter = '%(levelname)s : %(asctime)s :%(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)

# get date
class TimeManager(object):
    def GetDate(self):
        self.dt_now = datetime.date.today()
        logging.info(msg=type(self.dt_now))
        logging.info(msg=(self.dt_now))
        self.dt_str_now= self.dt_now.strftime('%Y-%m-%d')
        logging.info(msg=type(self.dt_str_now))
        return (self.dt_str_now)


# test for TimeManager
if __name__ == '__main__':
    tm = TimeManager()
    tm.GetDate()
    print(tm.GetDate())
