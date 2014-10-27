from parser import *
from Sdp import *
test1 = """
MEGACO/1 [30.1.1.107]:2944 Transaction=550363{Context=-{Notify=AL2{ObservedEvents=2{19700108T00294801:al/of}}}}
"""
test2 = """
MEGACO/1 [30.1.1.107]:2944 Reply=274{Context=6{Modify=AL2,Modify=E65541}}
"""

test22 = """
!/1 [30.1.1.3]:19032 T=275 {C=7 {MF=AL1 {E=8{al/of{strict=exact},al/on{strict=exact},g/sc},SG{al/ri}}, MF=E65542 {SG{cg/rt}}}}K{274}
"""

test3 = """
MEGACO/1 [30.1.1.107]:2944 Reply=276{Context=7{Modify=AL1,Modify=E65542}}TransactionResponseAck{550365}
"""

test4 = """
!/1 [30.1.1.3]:19032 T=276 {C=7 {MF=AL1{SG{},M{O{MO=SR,nt/jit=100}}} , MF=E65542 {SG{},M{O{MO=SR,nt/jit=100}}}}}
"""

test5 = """
!/1 [30.1.1.3]:19032 T=272 {C=$ {A=AL2 {M{O{MO=SR}}}, A=$ {M{O{MO=RC,nt/jit=100},L{
    v=0
    c=IN IP4 $
    m=audio $ RTP/AVP 18
    a=silenceSupp:off
    a=ptime:20
}}}}}
"""

test6 = """
!/1 [192.168.225.205]:10301 T=1422958{C=-{MF=AlcatelSP103001{E=1111{al/of{strict=state}},SG{}}}}
"""

test7 = """
!/1 [192.168.225.205]:10301
T=1422966{
    C=-{MF=AlcatelSP103004{SG{andisp/data{db=82060B010013010058,tas=dt}}}}}
"""


test8 = """
!/1 [192.168.225.205]:10301
T=1422968{
    C=-{MF=root{E=1199{it/ito{mit=2100}}}}}
"""
res =  megacoMessage.parseString(test5)
print res.sdp_string
#print message.parseString(testMessage)
# print message.parseString(test4)
# print commandRequestList.parseString("MF=AL1 , MF=E65542 {SG{},M{O{MO=SR,nt/jit=100}}}")
