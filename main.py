import fcal
import datetime

if __name__ == '__main__':
    c = fcal.fcal()
    for i in range(12):
        c.print_cal_with_day(datetime.datetime(2023, i+1, 2))
