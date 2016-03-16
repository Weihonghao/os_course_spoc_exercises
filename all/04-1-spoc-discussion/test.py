# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

data = dict()
pde_base = '11'


def addr_split(addr):
    s_addr = bin(int(addr, 16))[2:].zfill(15)
    return s_addr[:5], s_addr[5:10], s_addr[-5:]


def p1_index(off):
    global data
    return data[pde_base][int(off, 2)]


def phy_index(pde, off):
    b = bin(int(pde, 16))[2:].zfill(8)
    if b[0] == '0':
        return -1
    else:
        h1 = str(hex(int(b[1:4], 2))[2:])
        h2 = str(hex(int(b[4:], 2))[2:])
        return data[h1 + h2][int(off, 2)]


def find_value(addr):
    p1, p2, o = addr_split(addr)
    pde = p1_index(p1)
    pte = phy_index(pde, p2)
    if pte == -1:
        return -1
    pad = phy_index(pte, o)
    if pad == -1:
        return -1
    return pad


if __name__ == "__main__":
    data = dict()
    f = open("./03-2-data.txt")
    line = f.readline()
    while True:
        if line:
            content = line.split(": ")
            page_index = content[0].split()
            data[page_index[1]] = content[1].split()
            line = f.readline()
        else:
            break
    f.close()
    print(find_value("03df"))
    print(find_value("69dc"))