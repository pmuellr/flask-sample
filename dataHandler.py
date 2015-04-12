import os
import sys
import string

#-------------------------------------------------------------------------------
class DataHandler:

    #---------------------------------------------------------------------------
    def __init__(self, max=100):
        self.max  = max
        self.data = []

    #---------------------------------------------------------------------------
    def put(self, datum):
        while len(self.data) >= self.max:
            self.data.pop(0)

        self.data.append(datum)

    #---------------------------------------------------------------------------
    def get(self):
        return self.data

#-------------------------------------------------------------------------------
def main():
    max = 10
    add = 20

    dh = DataHandler(max=max)

    for i in xrange(0, add):
        dh.put(i)

    expected = add - max

    data = dh.get()
    for datum in data:
        print "got %d" % datum
        if datum is not expected:
            print "expected %d, but got %d" % (expected, datum)

        expected += 1

    return

#-------------------------------------------------------------------------------
if __name__ == "__main__": main()
