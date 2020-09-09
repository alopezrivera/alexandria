import datetime as dt

from mathematics.interpolation import derivative


"""
datetime manipulations
"""


def to_datetime(dates):
    return [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]


def from_datetime(dt_objs, format='%Y-%m-%d'):
    return [dt.datetime.strftime(d, format) for d in dt_objs]


def to_float(dates, year_0=2012):
    _d = []
    for date in dates:
        d = str(date).split('-')
        d = (float(d[0])-2020)*365 + float(d[1])*30 + float(d[2])
        _d.append(d)
    return _d


"""
Numerical methods
"""


def time_series_derivative(x, y):
    return derivative(to_float(x), to_float(y))

