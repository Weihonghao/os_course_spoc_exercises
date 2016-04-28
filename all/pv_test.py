#coding=utf-8
#!/usr/bin/env python

import threading
import time

condition1 = threading.Condition()

condition2 = threading.Condition()
frame = 0
wheel = 0
N = 10

class Worker1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition1, frame
        while True:
            if condition1.acquire():
                if frame < N - 1:
                    frame += 1;
                    print "Worker1(%s):deliver one1, now products:%s" %(self.name, frame)
                    print ""
                    condition1.notify()
                else:
                    print "Worker1(%s):already 9, stop deliver, now products:%s" %(self.name, frame)
                    condition1.wait();
                condition1.release()
                time.sleep(2)

class Worker2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition2, wheel
        while True:
            if condition2.acquire():
                if wheel < N-2:
                    wheel += 1;
                    print "Worker2(%s):deliver one2, now products:%s" %(self.name, wheel)
                    print ""
                    condition2.notify()
                else:
                    print "Worker2(%s):already 8, stop deliver, now products:%s" %(self.name, wheel)
                    condition2.wait();
                condition2.release()
                time.sleep(2)
class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition1, condition2, frame, wheel
        while True:
            if condition1.acquire():
                if frame > 1:
                    frame -= 1
                    print "!!!!!!!!!!!Consumer(%s):consume frame, now frame:%s, wheel:%s" %(self.name, frame,wheel)
                    condition1.notify()
                else:
                    print "Consumer(%s): stop consume frame, frame:%s,wheel:%s" %(self.name, frame,wheel)
                    condition1.wait();
                condition1.release()
                time.sleep(2)
            if condition2.acquire():
                if wheel > 2:
                    wheel-=2
                    print "$$$$$$$$$$$Consumer(%s):consume wheels and create a car, now frame:%s, wheel:%s" %(self.name, frame,wheel)
                    condition2.notify()
                else:
                    print "Consumer(%s): stop consume wheels, frame:%s,wheel:%s" %(self.name, frame,wheel)
                    condition2.wait();
                condition2.release()
                time.sleep(2)

if __name__ == "__main__":
    p1 = Worker1()
    p1.start()
    p2 = Worker2()
    p2.start()
    c = Consumer()
    c.start()