import time 
import random

def sleep():
    t = 0.01
    t += t * random.uniform(-t, t)  # Add some variance
    time.sleep(t)
N=100
sleep_time=0.1

# 					progress

print("Somebody talking to Prem while he is hungry: *exist*")
time.sleep(2)
print("Prem: *compute*")

from progress.bar import (Bar, ChargingBar, FillingSquaresBar,
                          FillingCirclesBar, IncrementalBar, PixelBar,
                          ShadyBar)
from progress.spinner import (Spinner, PieSpinner, MoonSpinner, LineSpinner,
                              PixelSpinner)
from progress.counter import Counter, Countdown, Stack, Pie



"""
bar = ChargingBar('Processing',max=N )
for i in range(0,N):
    time.sleep(sleep_time)
    bar.next()
bar.finish()
"""





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

"""
import progressbar
from time import sleep
bar = progressbar.ProgressBar(maxval=20, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
for i in xrange(20):
    bar.update(i+1)
    sleep(0.1)
bar.finish()
"""


#					TQDM
# https://notebooks.ai/ernest-galton/tqdm-ef22fcc1/lab
# https://github.com/tqdm/tqdm/wiki/How-to-make-a-great-Progress-Bar 
# https://pypi.org/project/tqdm/


from tqdm import tqdm


for i in tqdm(range(0,N)):
    sleep()
    
print("Prem: I don't give a fuck")   
print(" ¯\_(ツ)_/¯ ")