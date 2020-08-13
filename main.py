from asyncio import Queue

import mouse
import time
import random
import asyncio

from inputs import get_gamepad, GamePad

from inputs import devices

max = 2 ** 16


t1 = time.time()


if __name__ == "__main__":
    gamepad = devices.gamepads[0]
    x, y = 0, 0
    abs_x_prev, abs_y_prev = 0, 0
    while True:
        for events_batch in gamepad:
            for event in events_batch:
                x, y = 0, 0
                print(event.ev_type, event.code, event.state)
                c = 100
                if event.code == 'ABS_X':
                    curr_abx = event.state
                    x = c * (curr_abx - abs_x_prev) / max
                    abs_x_prev = event.state
                if event.code == 'ABS_Y':
                    curr_aby = event.state
                    y = c * (curr_aby - abs_y_prev) / max
                    abs_y_prev = event.state

                mouse.move(x, y, absolute=False)



