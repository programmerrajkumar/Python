from threading import *
from time import *
import logging


class OrderDetails:
    def __init__(self, products):
        self.ordersplaced = False
        self.products = products
        self.c = Condition()

    def Dispatch(self):
        for i in self.products:
            print("----Dispatching ", i, " ----")
            sleep(1)
        else:
            self.ordersplaced = True
            print("Orders Shipped Successfully")

    def Dispatch_Prime(self):
        self.c.acquire()
        for i in self.products:
            print("----Dispatching ", i, " ----")
            sleep(1)
        else:
            self.ordersplaced = True
            print("Orders Shipped Successfully")
        self.c.notify()
        self.c.release()


class Consumer:
    def __init__(self, orderDetails: OrderDetails):
        self.oderDetails = orderDetails

    def consume(self):
        while not self.oderDetails.ordersplaced:
            print("Waiting for Products")
            sleep(0.7)
        else:
            print("Received Order Successfully")

    def consume_prime(self):
        self.oderDetails.c.acquire()
        self.oderDetails.c.wait(timeout=0)
        self.oderDetails.c.release()
        print("Received Order Successfully")


o1 = OrderDetails(("Iphone", "Samsung Tab", "Clock"))
c1 = Consumer(o1)

t1 = Thread(target=o1.Dispatch)
t2 = Thread(target=c1.consume)

t1.start()
t2.start()

sleep(5)

t1 = Thread(target=o1.Dispatch_Prime)
t2 = Thread(target=c1.consume_prime)

t1.start()
t2.start()
