# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import threading
import random
import time
frame_num = 0
wheel_num = 0
empty_num = 5
s1_num = 3
s2_num = 4
# 参考https://github.com/chyyuu/ucore_os_lab/tree/master/related_info/lab7/semaphore_condition
mutex = threading.Lock()

# 是通过继承Thread类，重写它的run方法来创建Thread，第三种方法
class SemaphoreThread1(threading.Thread):

    # 这理semaphre是为了防止死锁，也就是说frame的数量不能够超过N-2
    def __init__(self, threadName, semaphore, empty, frame):
        # semaphore可以看成一个int，acquire时候-1，release的时候+1，如果是0的话就阻塞，可以大于初始值
        threading.Thread.__init__(self, name=threadName)
        self.s1 = semaphore  # 防止死锁的threshold
        self.empty = empty  # 空箱子的个数
        self.frame = frame  # 车架的数量

    def run(self):
        global frame_num, wheel_num, empty_num, s1_num, s2_num
        while True:
            time.sleep(2)
            self.s1.acquire()  # 防止死锁
            self.empty.acquire()  # 现在有空盒子
            if mutex.acquire():
                frame_num += 1
                s1_num -= 1
                empty_num -= 1
                print "Producer1(%s)\t%s\t%s\t%s\t%s\t%s" % (self.name, frame_num, wheel_num, empty_num, s1_num, s2_num)
                mutex.release()
            self.frame.release()  # 新增一个空架子


class SemaphoreThread2(threading.Thread):  # 轮子每次只是做一个，只是要两个才能凑成一对

    def __init__(self, threadName, semaphore, empty, wheel):
        threading.Thread.__init__(self, name=threadName)
        self.s2 = semaphore
        self.empty = empty
        self.wheel = wheel

    def run(self):
        global frame_num, wheel_num, empty_num, s1_num, s2_num
        while True:
            time.sleep(2.1)
            self.s2.acquire()
            self.empty.acquire()
            if mutex.acquire():
                wheel_num += 1
                s2_num -= 1
                empty_num -= 1
                print "Producer2(%s)\t%s\t%s\t%s\t%s\t%s" % (self.name, frame_num, wheel_num, empty_num, s1_num, s2_num)
                mutex.release()
            self.wheel.release()


class SemaphoreThread3(threading.Thread):

    def __init__(self, threadName, semaphore1, semaphore2, empty, frame, wheel):
        threading.Thread.__init__(self, name=threadName)
        self.s1 = semaphore1
        self.s2 = semaphore2
        self.empty = empty
        self.frame = frame
        self.wheel = wheel

    def run(self):
        global frame_num, wheel_num, empty_num, s1_num, s2_num
        while True:
            time.sleep(2.2)
            self.frame.acquire()
            self.wheel.acquire()
            self.wheel.acquire()
            if mutex.acquire():
                frame_num -= 1
                s1_num += 1
                empty_num += 1
                wheel_num -= 2
                s2_num += 2
                empty_num += 2
                print "Consumer(%s)\t%s\t%s\t%s\t%s\t%s" % (self.name, frame_num, wheel_num, empty_num, s1_num, s2_num)
                mutex.release()
            self.empty.release()
            self.s1.release()
            self.empty.release()
            self.empty.release()
            self.s2.release()
            self.s2.release()


if __name__ == "__main__":
    print 'who\tframe\twheel\tempty\ts1\ts2'
    s1 = threading.Semaphore(3)
    s2 = threading.Semaphore(4)
    Empty_sema = threading.Semaphore(5)
    Frame_sema = threading.Semaphore(0)
    Wheel_sema = threading.Semaphore(0)
    w1 = SemaphoreThread1("p1", s1, Empty_sema, Frame_sema)
    w1.start()
    w2 = SemaphoreThread2("p2", s2, Empty_sema, Wheel_sema)
    w2.start()
    w3 = SemaphoreThread3("p3", s1, s2, Empty_sema, Frame_sema, Wheel_sema)
    w3.start()
