# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Workingset:
    def __init__(self, win_size):
        self.win_size = win_size
        self.workingset = []

    def access(self, target):
        #print self.workingset, type(self.workingset), len(self.workingset)
        hit = False
        if target in self.workingset:
            hit = True
        if len(self.workingset) < self.win_size:
            self.workingset.append(target)
            #print 'test', self.workingset
        else:
            self.workingset = self.workingset[1:]
            self.workingset.append(target)
            #print 'test', self.workingset
        self.printInfo(target,hit)

    def printInfo(self, target, hit):
        if hit:
            print("access " + str(target) + " hit: " )
        else:
            print("access " + str(target) + " miss: ")
        print list(set(self.workingset))
        #print self.workingset

    def history(self, history_list):
        self.workingset = history_list


if __name__ == '__main__':
    test_sequence = ['c','c','d','b','c','e','c','e','a','d']
    print("------- Woring Set -------")
    ws = Workingset(4)
    ws.history(['e','d','a'])
    for target in test_sequence:
        ws.access(target)