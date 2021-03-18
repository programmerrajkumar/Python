from threading import *
from time import *


class Printer:

    def __init__(self):
        l=Lock()

    def display(self):
        threadname = current_thread().getName()
        i = 0
        print(threadname)
        sleep(0.2)
        while i < 6:
            print(threadname,i)
            i += 1


printer1 = Printer()
printer2 = Printer()

t1 = Thread(target=printer1.display)
t1.start()

t2 = Thread(target=printer2.display)
t2.start()
