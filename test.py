import pyparsing as pp
import unittest


class BasicTest(unittest.TestCase):
    def testWord(self):
        msg = "abc"
        word = pp.Word(pp.alphas)
        result = word.parseString(msg)
        self.assertEquals(1,1)

    def testLiteral(self):
        self.assertEquals(1,1)

    def testKeyword(self):
        self.assertEquals(1,1)


if __name__ == "__main__":
    unittest.main()
