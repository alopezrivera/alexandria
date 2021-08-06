import numpy as np
from math import ceil


# Angles
def deg(a):
    return a/np.pi*180


def rad(a):
    return a/180*np.pi


# Mass
def lbs_to_kg(m):
    return m*0.453592


# Conversion
def s_to_hms(_n):
    hours, remainder = divmod(_n, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f'{int(hours)}:{int(minutes)}:{seconds:.2f}'
