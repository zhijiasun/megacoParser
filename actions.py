from pyparsing import *
from megaco import *

transactionList = []
contextList = []
termList = []

def commandRequestListAction(tokens):
    print "commandRequestList"

def actionRequestAction(tokens):
    print "actionRequest"
    context = Context(tokens["ContextID"],termList)
    contextList.append(context)


def commandRequestAction(tokens):
    print "commandRequest"
    term = Termination(tokens["termID"],tokens["commandType"])
    termList.append(term)
    # print tokens.keys()
    # print tokens["termID"]

def megacoMessageAction(tokens):
    print "megacoMessageAction"
    print tokens.keys()
    tran = Transaction(tokens["transactionID"],contextList)
    transactionList.append(tran)

