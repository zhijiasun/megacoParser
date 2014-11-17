from parser import *
from Sdp import *


class Transaction:
    def __init__(self, tran_id, context, **kwargs):
        self.attrs = {}
        self.contextList = []
        self.attrs['tran_id'] = tran_id
        if type(context) is list:
            self.contextList = context
        else:
            self.contextList.append(context)
        self.attrs.update(kwargs)



class Context:
    def __init__(self, contextId, terms, **kwargs):
        self.contextId = contextId
        self.termList = []

        if type(terms) is list:
            self.termList = terms
        elif isinstance(terms, Termination):
            self.termList.append(terms)


class Command:
    def __init__(self, commandType, **kwargs):
        self.commandType = commandType


class Termination:
    def __init__(self, termId, commandType, **kwargs):
        self.termId = termId
        self.commandType = commandType
        self.contextId = None
        self.descriptorList = []


if __name__ == '__main__':
    t = Transaction(1345, version=1, ip='[192.168.1.1]:2944')
    print t.attrs
