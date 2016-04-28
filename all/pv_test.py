# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import threading
import time

condition1 = threading.Condition()

condition2 = threading.Condition()
frame = 0
wheel = 0
N = 12
# 参考https://github.com/chyyuu/ucore_os_lab/tree/master/related_info/lab7/semaphore_condition中的生产者和消费者模型


class Worker1(threading.Thread):  # 是通过继承Thread类，重写它的run方法来创建Thread，第三种方法

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition1, frame
        while True:
            if condition1.acquire():  # 通过acquire判断一些条件
                if frame < N - 2:  # 车架的数量不能够超过N-2
                    frame += 1
                    print "Worker1(%s):finished one frame, the number of the products:%s" % (self.name, frame)
                    condition1.notify()  # 条件满足，进行一些处理改变条件后，通过notify方法通知其他线程
                else:
                    print "Worker1(%s):already 11, waiting, now products:%s" % (self.name, frame)
                    condition1.wait()  # 条件不满足则wait
                condition1.release()
                time.sleep(3)


class Worker2(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition2, wheel
        while True:
            if condition2.acquire():
                if wheel < N - 1:  # 车轮的数量不能够超过N-1
                    wheel += 1  # 车轮也是一次只有一个的
                    print "Worker2(%s):finished two wheels, the number of the products:%s" % (self.name, wheel)
                    condition2.notify()
                else:
                    print "Worker2(%s):already 10, waiting, now products:%s" % (self.name, wheel)
                    condition2.wait()
                condition2.release()
                time.sleep(3)


class Worker3(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition1, condition2, frame, wheel
        while True:
            if condition1.acquire():
                if frame > 1:
                    frame -= 1
                    print "Worker3(%s):used one frame, now frame:%s, wheel:%s" % (self.name, frame, wheel)
                    condition1.notify()
                else:
                    print "Worker3(%s): waiting, frame:%s,wheel:%s----------------------------" % (self.name, frame, wheel)
                    condition1.wait()
                condition1.release()
                time.sleep(3)
            if condition2.acquire():
                if wheel > 2:
                    wheel -= 2
                    print "Worker3(%s):used two wheels, now frame:%s, wheel:%s" % (self.name, frame, wheel)
                    condition2.notify()
                else:
                    print "Worker3(%s): waiting, frame:%s,wheel:%s---------------------------------" % (self.name, frame, wheel)
                    condition2.wait()
                condition2.release()
                time.sleep(3)

if __name__ == "__main__":
    w1 = Worker1()
    w1.start()
    w2 = Worker2()
    w2.start()
    w3 = Worker3()
    w3.start()
