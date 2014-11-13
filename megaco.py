from parser import *
from Sdp import *


class Transaction:
    def __init__(self, tran_id, context, **kwargs):
        self.attrs = {}
        slef.contextList = []
        self.attrs['tran_id'] = tran_id
        if type(context) is list:
            self.contextList = context
        else:
            self.contextList.append(context)
        self.attrs.update(kwargs)


class Context:
    def __init__(self, contextId, **kwargs):
        self.contextId = contextId
        self.termList = []


class Command:
    def __init__(self, commandType, **kwargs):
        self.commandType = commandType


class Termination:
    def __init__(self, termId, **kwargs):
        self.termId = termId
        self.contextId = None
        self.commandType = None
        self.descriptorList = []


if __name__ == '__main__':
    t = Transaction(1345, version=1, ip='[192.168.1.1]:2944')
    print t.attrs
