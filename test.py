from pyparsing import *
import unittest


class BasicTest(unittest.TestCase):
    def testWord(self):
        pass


if __name__ == "__main__":
    domainAddress = "[" + Combine(Word(nums,max=3) + ((".")+Word(nums,max=3))*3) + "]"
    print domainAddress.parseString("[0.169.0.1]")

    exactString = Word(hexnums,max=8,exact=8)
    print exactString.parseString("9809abcd")

    test = domainAddress | exactString

    print test.parseString("[192.168.9.0]")
    test2 = OneOrMore(domainAddress | exactString)
    print test2.parseString("[192.168.9.0] 12345678 12345678 12345678")


