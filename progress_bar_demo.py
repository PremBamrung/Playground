import time 
import random


# 					progress


from progress.bar import (Bar, ChargingBar, FillingSquaresBar,
                          FillingCirclesBar, IncrementalBar, PixelBar,
                          ShadyBar)
from progress.spinner import (Spinner, PieSpinner, MoonSpinner, LineSpinner,
                              PixelSpinner)
from progress.counter import Counter, Countdown, Stack, Pie

N=100
sleep_time=0.1

"""
bar = ChargingBar('Processing',max=N )
for i in range(0,N):
    time.sleep(sleep_time)
    bar.next()
bar.finish()
"""


def sleep():
    t = 0.01
    t += t * random.uniform(-0.1, 0.1)  # Add some variance
    time.sleep(t)


for bar_cls in (Bar, ChargingBar, FillingSquaresBar, FillingCirclesBar):
    suffix = '%(index)d/%(max)d [%(elapsed)d / %(eta)d / %(eta_td)s]'
    bar = bar_cls(bar_cls.__name__, suffix=suffix)
    for i in bar.iter(range(200)):
        sleep()

for bar_cls in (IncrementalBar, PixelBar, ShadyBar):
    suffix = '%(percent)d%% [%(elapsed_td)s / %(eta)d / %(eta_td)s]'
    with bar_cls(bar_cls.__name__, suffix=suffix, max=200) as bar:
        for i in range(200):
            bar.next()
            sleep()

for spin in (Spinner, PieSpinner, MoonSpinner, LineSpinner, PixelSpinner):
    for i in spin(spin.__name__ + ' ').iter(range(100)):
        sleep()

for singleton in (Counter, Countdown, Stack, Pie):
    for i in singleton(singleton.__name__ + ' ').iter(range(100)):
        sleep()

bar = IncrementalBar('Random', suffix='%(index)d')
for i in range(100):
    bar.goto(random.randint(0, 100))
    sleep()
bar.finish()

#					TQDM
# https://notebooks.ai/ernest-galton/tqdm-ef22fcc1/lab
# https://github.com/tqdm/tqdm/wiki/How-to-make-a-great-Progress-Bar 
# https://pypi.org/project/tqdm/


from tqdm import tqdm


for i in tqdm(range(0,N)):
    sleep()
    
   