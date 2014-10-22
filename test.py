from pyparsing import *
import unittest


class BasicTest(unittest.TestCase):
    def testWord(self):
        pass


if __name__ == "__main__":
    domainAddress = "[" + Combine(Word(nums,max=3) + ((".")+Word(nums,max=3))*3) + "]"

    exactString = Word(hexnums,max=8,exact=8)

    test = domainAddress | exactString

    test2 = OneOrMore(domainAddress | exactString)
    
    test3 = exactString | domainAddress + Optional("," + exactString)
    print test3.parseString("[192.168.0.1]")

    test4 = Word(alphanums+"_",max=4)

    test5 = ZeroOrMore((Literal("|") | Literal("*")))
    print test5.parseString("||||****")

