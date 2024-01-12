__author__ = 'teacher'

from robot.body import mybody
from robot.head import myhead
from robot.leg import myleg

# from .body import mybody
# from .head import myhead
# from .leg import myleg

def integrate():
    print('로보트 합체 시작')
    myhead.get_head()
    mybody.get_body()
    myleg.get_leg()
    print('로보트 합체 끝!! 출동!!')