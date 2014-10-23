from parser import *

test1 = """
MEGACO/1 [30.1.1.107]:2944 Transaction=550363{Context=-{Notify=AL2{ObservedEvents=2{19700108T00294801:al/of}}}}
"""
test2 = """
!/1 [30.1.1.3]:19032 T=276 {C=7 {MF=AL1 , MF=E65542 {SG{},M{O{MO=SR,nt/jit=100}}}}}
"""

test3 = """
MEGACO/1 [30.1.1.107]:2944 Reply=276{Context=7{Modify=AL1,Modify=E65542}}TransactionResponseAck{550365}
"""

#print message.parseString(testMessage)
print message.parseString(test3)
