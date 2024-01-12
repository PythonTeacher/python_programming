# 패키지 : 관련된 모듈을 디렉토리 구조로 모아놓은 단위

# 패키지에 있는 모듈 가져오기

# 1. import 패키지명.모듈명 -> 사용시에도 다 써줌
import game.graphic.draw

game.graphic.draw.draw()

# 2. from 패키지명 import 모듈명 -> 모듈명.함수명
from game.graphic import draw

draw.draw()

# 3. from 패키지명.모듈명 import 함수명 -> 함수명만
from game.graphic.draw import draw

draw()

from game.sound import *

echo.echo()

# run -> draw와 echo모듈을 가져오자
from game.play import run

run.run()

# robot 패키지
# - head(myhead), body(mybody), leg(myleg) 패키지(모듈)
# 각 모듈에는 get_head(), get_body(), get_leg() 함수
# robot 패키지에 run.py를 만들고, integrate() 함수에서
# 로보트 조립을 완성해보자.

from robot import run

run.integrate()