from threading import *


class NumberPrinter:
    def PrintEvenNumbers(self, start, end):
        if start % 2 == 1: start += 1
        if end % 2 == 0: end += 1

        self.PrintRangeOfNumber(start, end, 2)

    def PrintOddNumbers(self, start, end):
        if start % 2 == 0: start += 1
        if end % 2 == 1: end += 1

        self.PrintRangeOfNumber(start, end, 2)

    def PrintNumbers(self, start, end):
        self.PrintRangeOfNumber(start, end + 1, 1)

    def PrintRangeOfNumber(self, start, end, step):
        threadname = "\n" + current_thread().name + " "
        for x in range(start, end, step):
            print(threadname + str(x))


printer = NumberPrinter()

oddthread = Thread(target=printer.PrintOddNumbers, args=(1, 100), name="OddThread")
eventhread = Thread(target=printer.PrintEvenNumbers, args=(1, 100), name="EvenThread")

oddthread.start()
# oddthread.join()
eventhread.start()
# eventhread.join()
printer.PrintNumbers(1, 100)
