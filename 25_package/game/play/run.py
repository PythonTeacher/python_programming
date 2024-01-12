__author__ = 'teacher'

from ..graphic import draw
from ..sound import echo

def run():
    print('run start')
    draw.draw()
    echo.echo()
    print('run end')