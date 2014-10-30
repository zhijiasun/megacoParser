from pyparsing import *
from parser import *
import os
import unittest


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



if __name__ == "__main__":
    test = """MEGACO/1 [20.8.1.204]:2944 Reply=39991317{Context=-{Modify=AL1{Error=430{}}}}"""
    test2 = """
    Context=-{Modify=AL1{Error=430{}}}
    """
    print actionReply.parseString(test2)
    # print megacoMessage.parseString(test)
    # read_wireshark("megacoString.txt")
    # for m in message:
        # try:
        #     print megacoMessage.parseString(m)
        # except Exception as e:
        #     print "*************************"
        #     print m
        #     print "*************************"
        #     print "parse error",e
