from pyparsing import *
from parser import *
from megaco import *
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


if __name__ == "__main__":
    test = """MEGACO/1 [20.8.1.204]:2944 Reply=39991317{Context=-{Modify=AL1{Error=430{}}}}"""
    test2 = """
    !/1 [10.0.55.41] T=40000572{C=-{O-AV=A1{AT{M }},O-AV=A2{AT{M }}},C=*{O-AV=A1{AT{M }},O-AV=A2{AT{M }}}}
    """
    # print actionReply.parseString(test2)
    result =  megacoMessage.parseString(test2)
    print result.keys()
    print result
    # print result['version'],result['ip'],result['port'],result['replyId'],result['contextId']

    # pytest()
