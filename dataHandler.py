import os
import sys
import json
import string

#-------------------------------------------------------------------------------
class DataHandler:

    #---------------------------------------------------------------------------
    def __init__(self, max=100):
        self.max   = max
        self.index = 0
        self.data  = []

    #---------------------------------------------------------------------------
    def put(self, datum):
        while len(self.data) >= self.max:
            self.data.pop(0)

        record = {}
        record['index'] = self.index
        record['datum'] = datum
        self.data.append(record)

        self.index += 1

    #---------------------------------------------------------------------------
    def get(self):
        return self.data

#-------------------------------------------------------------------------------
def main():
    max = 10
    add = 20

    dh = DataHandler(max=max)

    for i in xrange(0, add):
        dh.put(-i)

    expected = add - max

    data = dh.get()
    for record in data:
        datum = record['datum']
        index = record['index']

        print "record: %s" % json.dumps(record)

        if index is not expected:
            print "expected index %d, but got %d" % (expected, index)
        if -datum is not expected:
            print "expected datum %d, but got %d" % (expected, datum)

        expected += 1

    return

#-------------------------------------------------------------------------------
if __name__ == "__main__": main()
