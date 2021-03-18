from threading import  *

class MyThread(Thread):
    def run(self) -> None: #override base method
        i=0
        while i<10:
            print(current_thread().getName(), i)
            i+=1


t=MyThread()
t.start()
t1=MyThread()
t1.start()
#t.run() will run on main thread . new thread will not spawn(create and run in new thread)
