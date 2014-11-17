from pyparsing import *
from parser import *
from megaco import *
from actions import *
import os
import unittest


def pytest():
    w = Word(alphas)("test")
    n = Word(nums)("nums")
    r = delimitedList((w+n)("ll"),)("r")
    s = "a1,b2"
    result = r.parseString(s)
    print result



class BasicTest(unittest.TestCase):
    def testWord(self):
        pass


messageTime = []
message = []

commandRequestLength = 0


def read_wireshark(filepath):
    megaco_file = open(filepath)
    content = megaco_file.read()
    s = content.split("\n\n")
    for i in range(len(s)):
        c = []
        if i % 2 is 0:
            line = s[i].split("\n")
            # print k[1].split()[1]
            t = line[1].split()[1]
            messageTime.append(t)
        else:
            line = s[i].split("-------------- (RAW text output) ---------------\n")
            msg = line[1]
            message.append(msg)


def parse_file():
    read_wireshark("megacoString.txt")
    for m in message:
        if m.find("truncated") is not -1:
            print "message is truncated,not parse!!!"
            continue
        try:
            print megacoMessage.parseString(m)
        except Exception as e:
            print "parse error", e


transactionListNum = 0
actionRequestNum = 0
commandRequestListNum = 0


if __name__ == "__main__":
    test = """MEGACO/1 [20.8.1.204]:2944 Reply=39991317{Context=-{Modify=AL1{Error=430{}}}}"""
    test2 = """
    !/1 [10.0.55.41] T=40000572{C=-{O-AV=A1{AT{M }},O-AV=A2{AT{M }}},C=*{O-AV=A1{AT{M }},O-AV=A2{AT{M }}}}
    """
    test3 = """
    MEGACO/1 [20.8.1.204]:2944 Transaction=410950{Context=-{ServiceChange=ROOT{Services{Method=Restart,Reason="901 Cold Boot",ServiceChangeAddress=2944,Profile=AGW/1,Version=2,20121025T15230101}}}}
    """
    test4 = """
    !/1 [10.0.55.41] T=39991301{C=-{MF=AL9{E=589829{al/of{strict=exact,EM{SG{cg/dt},E=393217{dd/ce{ DM=shanghai1},al/on{strict=exact},g/sc}}},al/on{strict=exact}}}}}
    """
    # print actionReply.parseString(test2)
    result =  megacoMessage.parseString(test4)
    # transactionListNum = len(result["transactionList"])
    # actionRequestNum = len(result["actionRequest"])
    # commandRequestListNum = len(result["commandRequestList"])
    # print transactionListNum,actionRequestNum,commandRequestListNum
    for t in transactionList:
        print t.get_ctx_term_cmd()

    # for i in range(transactionListNum):
    #     transactionList_temp = result["transactionList"][i]
    #     for i in len(actionRequestNum):
    #         actionRequest_temp = transactionList_temp["actionRequest"]


    # pytest()
