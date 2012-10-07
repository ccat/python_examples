# encoding=utf-8
#-------------------------------------------------------------------------------
# Description:
# Author:      ccat
# Created:     25/Aug/2012
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
"""Example 1: Basic usage """

def generator1():
    yield "a"
    yield "b"
    yield "c"
    yield "d"
    yield "e"

gen=generator1()

print gen.next()
print gen.next()
print gen.next()

print ("FOR example")
gen2=generator1()
for i in gen2:
    print i

print ("Try Except example")
gen3=generator1()
try:
    while(True):print gen3.next()
except StopIteration:
    print("no more item")

first=1
diffs=1

print ("eternal loop example "+str(first)+" "+str(diffs))

#
def generateNextSequenceNum(First,diff):
    now=First
    while(True):
        yield now
        now+=diff

gen4=generateNextSequenceNum(first,diffs)

print gen4.next()
print gen4.next()
print gen4.next()
print gen4.next()

#-------------------------------------------------------------------------------
"""Example 2: Using in class """

print ("GeneratorClass example")

class GeneratorClass(object):
    def __init__(self):
        self.currentInt=0
        self.flag=True
        self.decInc=self.decIncGen()
    def decIncGen(self):
        while(self.flag):
            self.currentInt+=1
            yield self.currentInt
        while(self.currentInt>0):
            self.currentInt-=1
            yield self.currentInt
        return

gc=GeneratorClass()
for i in range(5):
    print gc.decInc.next()
gc.flag=False

for i in  gc.decInc:
    print i


#-------------------------------------------------------------------------------
"""Example 3: yield in yield """


def internalGenerator():
    for i in range(5):
        yield i

def outernalGenerator1():
    yield "start outernalGenerator1"
    tempGen=internalGenerator()
    yield tempGen.next()
    yield "end"

def outernalGenerator2():
    yield "start outernalGenerator2"
    tempGen=internalGenerator()
    for i in tempGen:
        yield i
    yield "end"

tempGen=outernalGenerator1()
for i in tempGen:
    print i

tempGen=outernalGenerator2()
for i in tempGen:
    print i

#-------------------------------------------------------------------------------
"""Example 4: Generator cannot be pickled """

import pickle

tempGen=outernalGenerator2()

print pickle.dumps(tempGen)


