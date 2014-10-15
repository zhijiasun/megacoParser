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

    def testSafeChar(self):
        SafeChar = pp.Word(pp.alphanums+"+ - & ! / \ ? @ ^ ` ~ * $ \( \) \" % \| .") 
        testStr = """f|adf"*&^%$""" 
        print SafeChar.parseString(testStr)
        self.assertEquals(1,1)

    def testQuotedString(self):
        self.assertEquals(1,1)



if __name__ == "__main__":
    AddToken = "Add" or "A"
    name = pp.Word(pp.alphas) + AddToken + pp.Word(pp.alphas)
    print name.parseString("fadf Afadsf")
    unittest.main()


