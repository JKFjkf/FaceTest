import datetime

def dayofyear():
    year = input('year:')
    month = input('month:')
    days = input('day:')
    data_1 = datetime.date(year=int(year),month=int(month),day=int(days))
    data_2 = datetime.date(year=int(year),month=1,day=1)
    print((data_1-data_2).days+1)
if __name__ == '__main__':
    dayofyear()