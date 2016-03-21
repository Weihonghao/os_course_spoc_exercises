# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import copy

class PageDefaultFrequency:
    def __init__(self, win_size):
        self.win_size = win_size
        self.workingset = []
        self.last = -1
        self.current = -1
        self.visitsequence = []
    def access(self, target):
        self.current += 1
        hit = False
        if target in self.workingset:
            hit = True
        if not hit:
            if self.current - self.last <= self.win_size:
                self.workingset.append(target)
            else:
                self.workingset = copy.deepcopy(self.visitsequence)
                self.workingset.append(target)
            self.last = self.current
        if len(self.visitsequence) == 2:
            self.visitsequence = self.visitsequence[1:]
        self.visitsequence.append(target)
        self.printInfo(target,hit)


    def printInfo(self, target, hit):
        if hit:
            print("access " + str(target) + " hit: " )
        else:
            print("access " + str(target) + " miss: ")
        #print list(set(self.workingset))
        print self.workingset

    def history(self, history_list):
        self.workingset = history_list

'''class PageFaultFrequency:
    def __init__(self, window_size):
        self.window_size = window_size
        self.history = []
        self.last_fault = 0
        self.current = -1
        self.mem = []

    def access(self, addr):
        self.history.append(addr)
        self.current += 1
        if len(self.history) > self.window_size + 1:
            del self.history[0]

        hit = True
        if addr not in self.mem:
            hit = False
            delta = self.current - self.last_fault
            self.last_fault = self.current

            if delta <= self.window_size:
                self.mem.append(addr)
            else:
                new_mem = []
                for i in self.mem:
                    if i in self.history:
                        new_mem.append(i)
                self.mem = new_mem
                self.mem.append(addr)
        self.printInfo(addr, hit)

    def printInfo(self, addr, hit):
        if hit:
            print("access " + str(addr) + " (H) " + ":"),
        else:
            print("access " + str(addr) + " (M) " + ":"),
        for i in self.mem:
            print(i),
        print("")'''



if __name__ == '__main__':
    test_sequence = ['c','c','d','b','c','e','c','e','a','d']
    print("------- page default frequency -------")
    ws = PageDefaultFrequency(2)
    ws.history(['e','d','a'])
    for target in test_sequence:
        ws.access(target)