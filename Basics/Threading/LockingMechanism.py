from threading import *
from  time import *

class BookMyBus:
    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        self.lock = Lock()

    def buy(self, requestedSeats):
        if self.availableSeats < requestedSeats:
            print("all seats are sold out")
            return

        self.lock.acquire(blocking=True)
        print("Confirming ", requestedSeats, " Seats")
        sleep(3)
        print("Processing the payments")
        print("Printing the tickets")
        self.availableSeats -= requestedSeats
        self.lock.release()


obj = BookMyBus(15)
t1 = Thread(target=obj.buy, args=(2,))
t2 = Thread(target=obj.buy, args=(3,))
t3 = Thread(target=obj.buy, args=(2,))
t1.start()
t2.start()
t3.start()
