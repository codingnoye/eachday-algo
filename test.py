import pyautogui as pg
import time
from pynput.keyboard import Key, Controller, Listener
global points
points = [
    (1318, 742), # 예매하기 버튼
    (195, 287), # 7월 11일
    (786, 635), # 다음단계
    (444, 519), # 적당한 자리로 미리 이동
    (786, 641) # 좌석선택완료
]
def on_press(key_origin):
    key = key_origin.__str__()
    print('{} key pressed'.format(key))
    if key=="'`'":
        print(pg.position())
    elif key=="'1'":
        pg.click(x=points[0][0], y=points[0][1])
    elif key=="'2'":
        pg.click(x=points[1][0], y=points[1][1])
    elif key=="'3'":
        pg.click(x=points[2][0], y=points[2][1])
        pg.click(x=points[3][0], y=points[3][1])
    elif key=="'4'":
        pg.click(x=points[4][0], y=points[4][1])
    
with Listener(on_press=on_press) as listener:
    listener.join()