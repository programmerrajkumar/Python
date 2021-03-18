import logging

logging.basicConfig(filename= "ExceptionHandling.txt", level=logging.DEBUG)


# f = None
class MinimunNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg


try:
    f = open("demofile.txt", "wt")
    f.write("Lorum Ipsum")

    x = -1
    if x < 0:
        raise MinimunNumberError("Sorry, no numbers below zero")

    x = "hello"

    if not type(x) is int:
        raise TypeError("Only integers are allowed")
except TypeError as ex:
    print(ex)
except MinimunNumberError as ex:
    print("Something went wrong when writing to the file", ex)
else:
    print("Updated file successfully")
finally:
    if f is not None:
        f.close()

try:
    logging.critical("critical")
    logging.error("error")
    logging.warning("warning")
    logging.info("info")
    logging.debug("debug")
except Exception as ex:
    print(ex)
