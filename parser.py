from pyparsing import *
from actions import *

AddToken = Literal("Add") | Literal("A")
AndAUDITselectToken = Literal("ANDLgc")
AuditToken = Literal("Audit") | Literal("AT")
AuditCapToken = Literal("AuditCapability") |  Literal("AC")
AuditValueToken = Literal("AuditValue") | Literal("AV")
AuthToken = Literal("Authentication") | Literal("AU")
BothwayToken = Literal("Bothway") | Literal("BW")
BriefToken = Literal("Brief") | Literal("BR")
BufferToken = Literal("Buffer") | Literal("BF")
CtxToken = Literal("Context") | Literal("C")
ContextAttrToken = Literal("ContextAttr") | Literal("CT") 
ContextListToken = Literal("ContextList") | Literal("CLT")
ContextAuditToken = Literal("ContextAudit") | Literal("CA")
DigitMapToken = Literal("DigitMap") | Literal("DM")
DisconnectedToken = Literal("Disconnected") | Literal("DC")
DelayToken = Literal("Delay") | Literal("DL")
DurationToken = Literal("Duration") | Literal("DR")
EmbedToken = Literal("Embed") | Literal("EM")
EmergencyToken = Literal("Emergency") | Literal("EG")
EmergencyOffToken = Literal("EmergencyOff") | Literal("EGO")
EmergencyValueToken  = Literal("EmergencyValue") | Literal("EGV") 
ErrorToken = Literal("Error") | Literal("ER")
EventBufferToken = Literal("EventBuffer") | Literal("EB")
EventsToken = Literal("Events") | Literal("E")
FailoverToken = Literal("Failover") | Literal("FL")
ForcedToken = Literal("Forced") | Literal("FO")
GracefulToken = Literal("Graceful") | Literal("GR")
H221Token = Literal("H221")
H223Token = Literal("H223")
H226Token = Literal("H226")
HandOffToken = Literal("HandOff") | Literal("HO")
IEPSToken = Literal("IEPSCall") | Literal("IEPS")
ImmAckRequiredToken = Literal("ImmAckRequired") | Literal("IA")
InactiveToken = Literal("Inactive") | Literal("IN")
IsolateToken = Literal("Isolate") | Literal("IS")
InSvcToken = Literal("InService") | Literal("IV")
InterruptByEventToken = Literal("IntByEvent") | Literal("IBE")
InterruptByNewSignalsDescrToken = Literal("IntBySigDescr") | Literal("IBS")
IterationToken = Literal("Iteration") | Literal("IR")
KeepActiveToken = Literal("KeepActive") | Literal("KA")
LocalToken = Literal("Local") | Literal("L")
LocalControlToken = Literal("LocalControl") | Literal("O")
LockStepToken = Literal("LockStep") | Literal("SP")
LoopbackToken = Literal("Loopback") | Literal("LB")
MediaToken = Literal("Media") | Literal("M")
MegacopToken = Literal("MEGACO") | Literal("!")
MessageSegmentToken = Literal("Segment") | Literal("SM")
MethodToken = Literal("Method") | Literal("MT")
MgcIdToken = Literal("MgcIdToTry") | Literal("MG")
ModeToken = Literal("Mode") | Literal("MO")
ModifyToken = Literal("Modify") | Literal("MF")
ModemToken = Literal("Modem") | Literal("MD")
MoveToken = Literal("Move") | Literal("MV")
MTPToken = Literal("MTP")
MuxToken = Literal("Mux") | Literal("MX")
NotifyToken = Literal("Notify") | Literal("N")
NotifyCompletionToken = Literal("NotifyCompletion") | Literal("NC")
ObservedEventsToken   = Literal("ObservedEvents") | Literal("OE")
OnewayToken           = Literal("Oneway") | Literal("OW")
OnewayBothToken   = Literal("OnewayBoth") | Literal("OWB") 
OnewayExternalToken  = Literal("OnewayExternal") | Literal("OWE")
OnOffToken            = Literal("OnOff") | Literal("OO")
OrAUDITselectToken = Literal("ORLgc")
OtherReasonToken      = Literal("OtherReason") | Literal("OR")
OutOfSvcToken         = Literal("OutOfService") | Literal("OS")
PackagesToken         = Literal("Packages") | Literal("PG")
PendingToken = Literal("Pending") | Literal("PN")
PriorityToken = Literal("Priority") | Literal("PR")
ProfileToken = Literal("Profile") | Literal("PF")
ReasonToken = Literal("Reason") | Literal("RE")
RecvonlyToken = Literal("ReceiveOnly") | Literal("RC")
ReplyToken = Literal("Reply") | Literal("P")
RestartToken = Literal("Restart") | Literal("RS")
RemoteToken = Literal("Remote") | Literal("R")
RequestIDToken = Literal("SPARequestID") | Literal("SPARQ")
ReservedGroupToken = Literal("ReservedGroup") | Literal("RG")
ReservedValueToken = Literal("ReservedValue") | Literal("RV")
SegmentationCompleteToken = Literal("END") | Literal("&")
SendonlyToken = Literal("SendOnly") | Literal("SO")
SendrecvToken = Literal("SendReceive") | Literal("SR")
ServicesToken = Literal("Services") | Literal("SV")
ServiceStatesToken = Literal("ServiceStates") | Literal("SI")
ServiceChangeIncompleteToken = Literal("ServiceChangeInc") | Literal("SIC")
ServiceChangeToken = Literal("ServiceChange") | Literal("SC")
ServiceChangeAddressToken = Literal("ServiceChangeAddress") | Literal("AD")
SignalListToken = Literal("SignalList") | Literal("SL")
SignalsToken = Literal("Signals") | Literal("SG")
SignalTypeToken = Literal("SignalType") | Literal("SY")
StatsToken = Literal("Statistics") | Literal("SA")
StreamToken = Literal("Stream") | Literal("ST")
SubtractToken = Literal("Subtract") | Literal("S")
SynchISDNToken = Literal("SynchISDN") | Literal("SN")
TerminationStateToken = Literal("TerminationState") | Literal("TS")
TestToken = Literal("Test") | Literal("TE")
TimeOutToken = Literal("TimeOut") | Literal("TO")
TopologyToken = Literal("Topology") | Literal("TP")
TransToken = Literal("Transaction") | Literal("T")
ResponseAckToken = Literal("TransactionResponseAck") |  Literal("K")
V18Token = Literal("V18")
V22Token = Literal("V22")
V22bisToken = Literal("V22b")
V32Token = Literal("V32")
V32bisToken = Literal("V32b")
V34Token = Literal("V34")
V76Token = Literal("V76")
V90Token = Literal("V90")
V91Token = Literal("V91")
VersionToken = Literal("Version") | Literal("V")


LBRKT = Literal("{")
RBRKT = Literal("}")
LSBRKT = Literal("[")
RSBRKT = Literal("]")
EQUAL = Literal("=")
COLON = Literal(":")
SLASH = Literal("/")
COMMA = Literal(",")
DOT = Literal(".")
DIGIT = nums
nonEscapeChar = "}" + srange("[\\0x01-\\0x7c]") #+ srange("[\\0x7E-\\0xFF]")
nonEscapeChar = srange("[\\0x01-\\0x7c]") #+ srange("[\\0x7E-\\0xFF]")
octetString = Word(nonEscapeChar)
# octetString = Word("}" + srange("[\\0x01-\\0x7c]")) #+ srange("[\\0x7E-\\0xFF]"))
INEQUAL = Literal(">") | Literal("<") | Literal("#")
RestChar = "; [ ] { } : , # < > ="
authenticationHeader = AuthToken + EQUAL + Literal("0x") + Word(hexnums,min=8,exact=8) + COLON +Literal("0x") + Word(hexnums,min=8,max=8) + \
        COLON + Word(hexnums,min=24,max=64)
Timer = Word(nums,min=1,max=2)
Date = Word(nums,min=8,max=8)
Time = Word(nums,min=8,max=8)
TimeStamp = Date + "T" + Time
quotedString = dblQuotedString
VALUE = quotedString | Word(alphanums+"+ - & ! / \ ? @ ^ ` ~ * $ \( \) \" % \| .",min=1)
extensionParameter = Literal("X") + (Literal("-") | Literal("+")) + Word(alphanums,min=1,max=6)
Version = Word(nums,min=1,max=2)
COMMENT = Literal(";") + Word(alphanums+"+ - & ! / \ ? @ ^ ` ~ * $ \( \) \" % \| .")
domainAddress = Suppress(Literal("[")) + Combine(Word(nums,max=3) + (Literal(".")+Word(nums,max=3))*3)("ip") + Suppress(Literal("]"))
domainName = Literal("<") + Combine(Word(alphanums)+Word(alphanums+"- .",max=63)) + Literal(">")
portNumber = Word(nums)("port")
mId = (domainAddress | domainName)+Optional(":"+portNumber)

TransactionID = (Word(nums, max=32))("transactionID")
ContextID = (Word(nums, max=32) | Literal("*") | Literal("-") | Literal("$"))("ContextID")
NAME = Word(alphanums + "_",max=64) # how to confirm the first character is an alphas ???
PackageName = NAME
ItemID = NAME
digitMapName = NAME
pathDomainName = Word(alphanums+"*",min=1,max=1) + Word(alphanums+"-",max=63)
pathNAME = Optional(Literal("*")) + NAME + ZeroOrMore(Literal("|") | Literal("*") | Word(alphanums) | Literal("_") | Literal("$")) + Optional(Literal("@") + pathDomainName)
TerminationID = (Literal("ROOT") | pathNAME | Literal("$") | Literal("*"))("termID")

RequestID = Word(nums,max=32) | Literal("*")
StreamID = Word(nums,max=16)
signalListId = Word(nums,max=16)

pkgdName = (PackageName + SLASH + ItemID) | (PackageName + SLASH + Literal("*")) | (Literal("*") + SLASH + Literal("*"))
signalName = pkgdName
sigStream = StreamToken + EQUAL + StreamID
sigParameterName = NAME
alternativeValue = (VALUE | (LSBRKT + delimitedList(VALUE) + RSBRKT) | (LBRKT + delimitedList(VALUE) + RBRKT) | (LSBRKT + VALUE + COLON + VALUE + RSBRKT))
parmValue = ((EQUAL + alternativeValue) | (INEQUAL + VALUE))
propertyParm = pkgdName + parmValue
sigOther = sigParameterName + parmValue
sigDuration = DurationToken + EQUAL + Word(nums,max=16)
signalType = OnOffToken | TimeOutToken | BriefToken
sigSignalType = SignalTypeToken + EQUAL + signalType
notificationReason = TimeOutToken | InterruptByEventToken | InterruptByNewSignalsDescrToken | OtherReasonToken
notifyCompletion = NotifyCompletionToken + EQUAL + LBRKT + delimitedList(notificationReason) + RBRKT                                                                                               
sigParameter = sigStream | sigSignalType | sigDuration | sigOther | notifyCompletion | KeepActiveToken
signalRequest = signalName + Optional(LBRKT + delimitedList(sigParameter) + RBRKT)
signalListParm = signalRequest
signalList = SignalListToken + EQUAL + signalListId + LBRKT + delimitedList(signalListParm) + RBRKT
signalParm  = signalList | signalRequest
# signalsDescriptor = SignalsToken + Optional(LBRKT + delimitedList(signalParm) + RBRKT)
signalsDescriptor = SignalsToken + LBRKT + Optional(delimitedList(signalParm)) + RBRKT
embedSig = EmbedToken + LBRKT + signalsDescriptor + RBRKT
eventStream = StreamToken + EQUAL + StreamID
eventParameterName = NAME
digitMapLetter = DIGIT # this should change,not complete
digitLetter = ZeroOrMore((DIGIT + Literal("-") + DIGIT) | digitMapLetter)
digitMapRange = Literal("x") | (LSBRKT + digitLetter + RSBRKT) 
digitPosition = digitMapLetter | digitMapRange
digitStringElement = digitPosition + Optional(DOT)
digitString = OneOrMore(digitStringElement)
digitStringList = delimitedList(digitString,delim="|")
digitMap = digitString | (Literal("(") + digitStringList + ")")
digitMapValue = Optional(Literal("T") + COLON + Timer + COMMA) + \
                Optional(Literal("S") + COLON + Timer + COMMA) + \
                Optional(Literal("L") + COLON + Timer + COMMA) + digitMap
eventOther = eventParameterName + parmValue
eventDM = DigitMapToken + EQUAL + ((digitMapName) | (LBRKT + digitMapValue + RBRKT))
secondEventParameter = embedSig | KeepActiveToken | eventDM | eventStream | eventOther
secondRequestedEvent = pkgdName + Optional(LBRKT + delimitedList(secondEventParameter) + RBRKT)
embedFirst = EventsToken + Optional(EQUAL + RequestID + LBRKT + delimitedList(secondRequestedEvent) + RBRKT)
embedWithSig = EmbedToken + LBRKT + signalsDescriptor + Optional(COMMA + embedFirst) + RBRKT
embedNoSig = EmbedToken + LBRKT + embedFirst + RBRKT
eventParameter = embedWithSig | embedNoSig | KeepActiveToken | eventDM | eventStream | eventOther
requestedEvent = pkgdName + Optional(LBRKT + delimitedList(eventParameter) + RBRKT)
eventsDescriptor = EventsToken + Optional(EQUAL + RequestID + LBRKT + delimitedList(requestedEvent) + RBRKT)

digitMapDescriptor = DigitMapToken + EQUAL + ((LBRKT + digitMapValue + RBRKT) | (digitMapName + Optional(LBRKT + digitMapValue + RBRKT)))
modemType = V32bisToken | V22bisToken | V18Token | V22Token | V32Token | V34Token | V90Token | V91Token | SynchISDNToken | extensionParameter
modemDescriptor = ModemToken + ((EQUAL + modemType) | (LSBRKT + delimitedList(modemType) + RSBRKT))\
                    + Optional(LBRKT + delimitedList(propertyParm) + RBRKT)

localDescriptor = LocalToken + LBRKT + octetString("sdp_string") + RBRKT
remoteDescriptor = RemoteToken + LBRKT + octetString("sdp_string") + RBRKT

streamModes = SendonlyToken | RecvonlyToken | SendrecvToken | InactiveToken | LoopbackToken
streamMode = ModeToken + EQUAL + streamModes

reservedValueMode = ReservedValueToken + EQUAL + (Literal("ON") | Literal("OFF"))
reservedGroupMode = ReservedGroupToken + EQUAL + (Literal("ON") | Literal("OFF"))

localParm = (streamMode | propertyParm | reservedValueMode | reservedGroupMode)
localControlDescriptor = LocalControlToken + LBRKT + delimitedList(localParm) + RBRKT

streamParm = (localDescriptor | remoteDescriptor | localControlDescriptor)
streamDescriptor = StreamToken + EQUAL + StreamID + LBRKT + delimitedList(streamParm) + RBRKT

serviceStates = ServiceStatesToken + EQUAL + (TestToken | OutOfSvcToken | InSvcToken)
eventBufferControl = BufferToken + EQUAL + (Literal("OFF") | LockStepToken)

terminationStateParm = propertyParm | serviceStates | eventBufferControl
terminationStateDescriptor = TerminationStateToken + LBRKT + delimitedList(terminationStateParm) + RBRKT

mediaParm = streamParm | streamDescriptor | terminationStateDescriptor
mediaDescriptor = MediaToken + LBRKT + delimitedList(mediaParm) + RBRKT

terminationIDList  = LBRKT + delimitedList(TerminationID) +  RBRKT
MuxType = H221Token | H223Token | H226Token | V76Token | extensionParameter
muxDescriptor = MuxToken + EQUAL + MuxType + terminationIDList

eventSpecParameter = eventStream | eventOther
eventSpec = pkgdName + Optional(LBRKT + delimitedList(eventSpecParameter) + RBRKT)
eventBufferDescriptor = EventBufferToken + Optional(LBRKT + delimitedList(eventSpec) + RBRKT)

indAudremoteDescriptor = RemoteToken + LBRKT + octetString + RBRKT
indAudlocalDescriptor = LocalToken + LBRKT + octetString + RBRKT
indAudlocalParm = (ModeToken + Optional((EQUAL | INEQUAL) + streamModes)) | pkgdName | propertyParm | ReservedValueToken | ReservedGroupToken
indAudlocalControlDescriptor = LocalControlToken + LBRKT + delimitedList(indAudlocalParm) + RBRKT
indAudstatisticsDescriptor = StatsToken + LBRKT + pkgdName + RBRKT
indAudstreamParm = indAudlocalControlDescriptor | indAudstatisticsDescriptor | indAudremoteDescriptor | indAudlocalDescriptor
indAudstreamDescriptor = StreamToken + EQUAL + StreamID + LBRKT + indAudstreamParm + RBRKT
serviceStatesValue = TestToken | OutOfSvcToken | InSvcToken
indAudterminationStateParm = pkgdName | propertyParm | ServiceStatesToken | Optional((EQUAL | INEQUAL) + serviceStatesValue) | BufferToken
indAudterminationStateDescriptor = TerminationStateToken + LBRKT + indAudterminationStateParm + RBRKT
indAudmediaParm = indAudstreamParm | indAudstreamDescriptor | indAudterminationStateDescriptor
indAudmediaDescriptor = MediaToken + LBRKT + delimitedList(indAudmediaParm) + RBRKT
indAudrequestedEvent = pkgdName
indAudeventsDescriptor = EventsToken + Optional(EQUAL + RequestID) + LBRKT + indAudrequestedEvent + RBRKT

sigRequestID = RequestIDToken + EQUAL + RequestID
indAudsignalRequestParm = sigStream | sigRequestID
indAudsignalRequest = signalName + Optional(LBRKT + delimitedList(indAudsignalRequestParm) + RBRKT)
indAudsignalListParm = indAudsignalRequest
indAudsignalList = SignalListToken + EQUAL + signalListId + Optional(LBRKT + indAudsignalListParm + RBRKT)
indAudsignalParm = indAudsignalList | indAudsignalRequest
indAudsignalsDescriptor = SignalsToken + LBRKT + Optional(indAudsignalParm) + RBRKT

indAuddigitMapDescriptor = DigitMapToken + EQUAL + digitMapName

indAudeventSpecParameter = eventStream | eventParameterName
indAudeventSpec = pkgdName + Optional(LBRKT + indAudeventSpecParameter + RBRKT)
indAudeventBufferDescriptor = EventBufferToken + LBRKT + indAudeventSpec + RBRKT

packagesItem = NAME + Literal("-") + Word(nums,max=16)
indAudpackagesDescriptor = PackagesToken + LBRKT + packagesItem + RBRKT
indAudauditReturnParameter = indAudmediaDescriptor | indAudeventsDescriptor | indAudsignalsDescriptor | indAuddigitMapDescriptor | indAudeventBufferDescriptor | \
                            indAudstatisticsDescriptor | indAudpackagesDescriptor
indAudterminationAudit = delimitedList(indAudauditReturnParameter)
auditReturnItem = MuxToken | ModemToken | MediaToken | DigitMapToken | StatsToken | ObservedEventsToken | PackagesToken
auditItem = auditReturnItem | SignalsToken | EventBufferToken | EventsToken | indAudterminationAudit
auditDescriptor = AuditToken + LBRKT + Optional(delimitedList(auditItem)) + RBRKT

ammParameter = mediaDescriptor | modemDescriptor | muxDescriptor | eventsDescriptor | signalsDescriptor | digitMapDescriptor | eventBufferDescriptor | auditDescriptor
ammRequest = (AddToken | MoveToken | ModifyToken )("commandType") + EQUAL + TerminationID + Optional(LBRKT + delimitedList(ammParameter) + RBRKT)
auditRequest = (AuditValueToken | AuditCapToken)("commandType") + EQUAL + TerminationID + LBRKT + auditDescriptor + RBRKT
subtractRequest = SubtractToken + EQUAL + TerminationID + Optional(LBRKT + auditDescriptor + RBRKT)

observedEventParameter = eventStream | eventOther
#observedEvent = Optional(TimeStamp + COLON) + pkgdName + Optional(delimitedList(LBRKT + observedEventParameter + RBRKT))
observedEvent = Optional(TimeStamp + COLON) + pkgdName + Optional(LBRKT + delimitedList(observedEventParameter) + RBRKT)
observedEventsDescriptor = ObservedEventsToken + EQUAL + RequestID + LBRKT + delimitedList(observedEvent) + RBRKT

ErrorCode = Word(nums,min=1,max=4)
errorDescriptor = ErrorToken + EQUAL + ErrorCode + LBRKT + Optional(quotedString) + RBRKT

serviceChangeAddress = ServiceChangeAddressToken + EQUAL + (mId | portNumber)
serviceChangeMgcId = MgcIdToken + EQUAL + mId
serviceChangeReason = ReasonToken + EQUAL + VALUE
serviceChangeDelay = DelayToken + EQUAL + Word(nums,max=32)
serviceChangeProfile = ProfileToken + EQUAL + NAME + SLASH + Version
serviceChangeVersion = VersionToken + EQUAL + Version
extension = extensionParameter + parmValue
servChgReplyParm = serviceChangeAddress | serviceChangeMgcId | serviceChangeProfile | serviceChangeVersion | TimeStamp
serviceChangeReplyDescriptor = ServicesToken + LBRKT + delimitedList(servChgReplyParm) + RBRKT

serviceChangeMethod = MethodToken + EQUAL + (FailoverToken | ForcedToken | GracefulToken | RestartToken | DisconnectedToken | HandOffToken | extensionParameter)
serviceChangeParm = serviceChangeMethod | serviceChangeReason | serviceChangeDelay | serviceChangeAddress | serviceChangeProfile | \
                    extension | TimeStamp | serviceChangeMgcId | serviceChangeVersion | ServiceChangeIncompleteToken | auditItem
serviceChangeDescriptor  = ServicesToken + LBRKT + delimitedList(serviceChangeParm) + RBRKT
serviceChangeRequest = ServiceChangeToken + EQUAL + TerminationID + LBRKT + serviceChangeDescriptor + RBRKT

notifyRequest = NotifyToken + EQUAL + TerminationID + LBRKT + observedEventsDescriptor + Optional(Literal(",")+errorDescriptor) + RBRKT
commandRequest = (ammRequest | subtractRequest | auditRequest | notifyRequest | serviceChangeRequest).setResultsName("commandRequest").setParseAction(commandRequestAction)
commandRequestList = (delimitedList(Optional(Literal("O-")) + Optional(Literal("W-")) + commandRequest)).setResultsName("commandRequestList",listAllMatches=True).setParseAction(commandRequestListAction)

packagesDescriptor = PackagesToken + LBRKT + delimitedList(packagesItem) + RBRKT
statisticsParameter = pkgdName + Optional((EQUAL + VALUE) | (LSBRKT + delimitedList(VALUE) + RSBRKT))
statisticsDescriptor = StatsToken + LBRKT + delimitedList(statisticsParameter) + RBRKT
auditReturnParameter = mediaDescriptor | modemDescriptor | muxDescriptor | errorDescriptor | eventsDescriptor | signalsDescriptor | digitMapDescriptor | observedEventsDescriptor | eventBufferDescriptor | statisticsDescriptor | packagesDescriptor | auditReturnItem
terminationAudit = delimitedList(auditReturnParameter)
ammsReply = (AddToken | MoveToken | ModifyToken | SubtractToken) + EQUAL + TerminationID + Optional(LBRKT + terminationAudit + RBRKT)

auditOther = EQUAL + TerminationID + Optional(LBRKT + terminationAudit + RBRKT)
contextTerminationAudit = EQUAL + CtxToken + (terminationIDList | (LBRKT + errorDescriptor + RBRKT))
auditReply = (AuditValueToken | AuditCapToken) + (contextTerminationAudit | auditOther)

notifyReply = NotifyToken + EQUAL + TerminationID + Optional(LBRKT + errorDescriptor + RBRKT)
serviceChangeReply = ServiceChangeToken + EQUAL + TerminationID + Optional(LBRKT + (errorDescriptor | serviceChangeReplyDescriptor) + RBRKT)

"""
context related definitions
"""
topologyDirection = BothwayToken | IsolateToken | OnewayToken | OnewayExternalToken | OnewayBothToken
topologyTriple = TerminationID + Literal(",") + TerminationID + topologyDirection
topologyDescriptor = TopologyToken + LBRKT + delimitedList(topologyTriple) + RBRKT
priority = PriorityToken + EQUAL + Word(nums, max=16)
iepsValue = IEPSToken + EQUAL + (Literal("ON") | Literal("OFF"))
emergencyValue = EmergencyValueToken + EQUAL + (EmergencyToken | EmergencyOffToken) 
contextIdList = ContextListToken + EQUAL + LBRKT + delimitedList(ContextID) + RBRKT
contextAttrDescriptor = ContextAttrToken + LBRKT + (contextIdList | delimitedList(propertyParm)) + RBRKT
contextProperty = topologyDescriptor | priority | EmergencyToken | EmergencyOffToken | iepsValue | contextAttrDescriptor
contextProperties = delimitedList(contextProperty)
auditSelectLogic = Optional((AndAUDITselectToken | OrAUDITselectToken)) 
contextAuditSelector = priority | emergencyValue | iepsValue | contextAttrDescriptor | auditSelectLogic
contextAuditProperties = TopologyToken | EmergencyToken | PriorityToken | IEPSToken | pkgdName | contextAuditSelector
indAudcontextAttrDescriptor = ContextAttrToken + LBRKT + delimitedList(contextAuditProperties) + RBRKT

contextAudit = ContextAuditToken + LBRKT + (delimitedList(contextAuditProperties) | indAudcontextAttrDescriptor ) + RBRKT
contextRequest = contextAudit | (contextProperties + Optional(Literal(",") + contextAudit))
actionRequest = (CtxToken + EQUAL + ContextID + LBRKT + ((contextRequest + Optional(Literal(",") + commandRequestList)) | commandRequestList) + RBRKT).setResultsName("actionRequest", listAllMatches=True).setParseAction(actionRequestAction)

transactionPending = PendingToken + EQUAL + TransactionID + LBRKT + RBRKT
transactionAck = TransactionID | (TransactionID + Literal("-") + TransactionID)
transactionResponseAck = ResponseAckToken + LBRKT + delimitedList(transactionAck) + RBRKT
transactionRequest = (TransToken + EQUAL + TransactionID + LBRKT + delimitedList((actionRequest)) + RBRKT)


commandReplys = serviceChangeReply | auditReply | ammsReply | notifyReply
commandReplyList = delimitedList(commandReplys)
commandReply = commandReplyList | (contextProperties + Optional(COMMA+commandReplyList))
actionReply = CtxToken + EQUAL + ContextID("contextId") + LBRKT + (errorDescriptor | commandReply | (commandReply + COMMA + errorDescriptor)) + RBRKT

actionReplyList = delimitedList(actionReply)
segmentNumber = Word(nums,max=16)
segmentReply = MessageSegmentToken + EQUAL + TransactionID + SLASH + segmentNumber + Optional(SLASH  + SegmentationCompleteToken)
transactionReply = ReplyToken + EQUAL + TransactionID("replyId") + Optional(SLASH +segmentNumber + Optional(SLASH + SegmentationCompleteToken)) + LBRKT + Optional(ImmAckRequiredToken + COMMA) + (errorDescriptor | actionReplyList) + RBRKT
transactionList = OneOrMore(transactionRequest | transactionReply | transactionPending | transactionResponseAck).setResultsName("transactionList",listAllMatches=True)
messageBody = errorDescriptor | transactionList
message = MegacopToken + SLASH + (Version)("version") + mId + messageBody
megacoMessage = (Optional(authenticationHeader) + message).setParseAction(megacoMessageAction)
