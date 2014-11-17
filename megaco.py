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

    def get_ctx_term_cmd(self):
        ctx_term_cmd = []
        for context in self.contextList:
            term_cmd = []
            cid = context.contextId
            for t in context.termList:
                print t.termId
                term_cmd.append((t.termId,t.commandType))
            ctx_term_cmd.append((cid,term_cmd))
            print ctx_term_cmd
            term_cmd = []
        return ctx_term_cmd




class Context:
    def __init__(self, contextId, terms, **kwargs):
        self.contextId = contextId
        self.termList = []

        if type(terms) is list:
            self.termList = terms
        elif isinstance(terms, Termination):
            self.termList.append(terms)
    @property
    def contextId(self):
        return self.contextId

    @property
    def termList(self):
        return self.termList


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
