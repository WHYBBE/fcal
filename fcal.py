import datetime


class fcal:
    def __init__(self):
        self.__cal_array = [
            [0,  0,  0,  0,  0,  0,  1,  2,  3,  4,  5,  6,  7],
            [2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14],
            [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
            [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
            [23, 24, 25, 26, 27, 28, 29, 30, 31,  0,  0,  0,  0],
            [30, 31,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        ]

        self.__month_text = ['January', 'February', 'March', 'April',
                             'May', 'June', 'July', 'August',
                             'September', 'October', 'November', 'December']

        self.__week_text = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']

    def print_cal(self, out_frame=True, width=3, type=0, date=[2023, 1, 1]):
        if type > 6 or type < 0:
            raise ValueError()
        if width > 10 or width < 3:
            raise ValueError()

        def print_outer_frame_line():
            print('+', '-'*(width*13+1), '+', sep='')

        def print_inner_frame_line():
            if out_frame:
                print('|', end='')
            print(' '*width*type, '+',  '-'*(width*7-1),
                  '+', ' '*width*(6-type), sep='', end='')
            if out_frame:
                print('|')
            else:
                print()

        def print_year_month_title():
            if out_frame:
                print('|', end='')
            print(' '*width*type, '|', sep='', end='')
            text = str(self.__month_text[date[1]-1])+' '+str(date[0])
            print(f'{text:^{width*7-1}}', end='')
            print('|', ' '*width*(6-type), sep='', end='')
            if out_frame:
                print('|')
            else:
                print()

        def print_week_title():
            if out_frame:
                print('|', end='')
            print(' '*width*type, '|', sep='', end='')
            for i in range(7):
                if (i == 0):
                    print(f'{self.__week_text[i]:>{width-1}}', end='')
                else:
                    print(f'{self.__week_text[i]:>{width}}', end='')
            print('|', ' '*width*(6-type), sep='', end='')
            if out_frame:
                print('|')
            else:
                print()

        if out_frame:
            print_outer_frame_line()
        print_inner_frame_line()
        print_year_month_title()
        print_week_title()
        for line in self.__cal_array:
            if out_frame:
                print('|', end='')
            for i in range(13):
                def print_day(day_width):
                    if line[i]:
                        print(f'{line[i]:>{day_width}}', end='')
                    else:
                        print(' '*day_width, end='')
                if (i == type):
                    print('|', end='')
                    print_day(width-1)
                elif (i == type+6):
                    print_day(width)
                    print('|', end='')
                elif (i == type+7):
                    print_day(width-1)
                else:
                    print_day(width)
            if (type != 6):
                print(' ', end='')
            if out_frame:
                print('|')
            else:
                print()
        print_inner_frame_line()
        if out_frame:
            print_outer_frame_line()

    def print_cal_with_day(self, date=datetime.datetime.today()):
        year = date.year
        month = date.month
        day = date.day
        week = datetime.date(year, month, 1).weekday()
        pos = 0
        if week == 6:
            pos = 6
        else:
            pos = 5 - week
        self.print_cal(type=pos, date=[year, month, day])
