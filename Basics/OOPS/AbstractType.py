from abc import *


class Phone(ABC):

    @abstractmethod
    def call(self):
        pass


class Iphone(Phone):

    def call(self):
        print("Iphone call")


iphone = Iphone()
iphone.call()
