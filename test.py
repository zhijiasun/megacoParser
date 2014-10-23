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

    test4 = Word(alphanums+"_",max=4)

    test5 = ZeroOrMore((Literal("|") | Literal("*")))

    NAME = Word(alphas,min=1,max=1) + Word(alphanums + "_",max=63)
    print NAME.parseString("a fad1")
