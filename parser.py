from pyparsing import *

AddToken = Literal("Add") | Literal("A")
AuditToken = Literal("Audit") | Literal("AT")
AuditCapToken = Literal("AuditCapability") |  Literal("AC")
AuditValueToken = Literal("AuditValue") | Literal("AV")
AuthToken = Literal("Authentication") | Literal("AU")
BothwayToken = Literal("Bothway") | Literal("BW")
BriefToken = Literal("Brief") | Literal("BR")
BufferToken = Literal("Buffer") | Literal("BF")
CtxToken = Literal("Context") | Literal("C")
ContextAuditToken = Literal("ContextAudit") | Literal("CA")
DigitMapToken = Literal("DigitMap") | Literal("DM")
DisconnectedToken = Literal("Disconnected") | Literal("DC")
DelayToken = Literal("Delay") | Literal("DL")
DurationToken = Literal("Duration") | Literal("DR")
EmbedToken = Literal("Embed") | Literal("EM")
EmergencyToken = ("Emergency") | Literal("EG")
ErrorToken = Literal("Error") | Literal("ER")
EventBufferToken = Literal("EventBuffer") | Literal("EB")
EventsToken = Literal("Events") | Literal("E")
FailoverToken              = ("Failover"               "FL")
ForcedToken                = ("Forced"                 "FO")
GracefulToken              = ("Graceful"               "GR")
H221Token                  = Literal("H221")
H223Token                  = Literal("H223")
H226Token                  = Literal("H226")
HandOffToken               = ("HandOff"                "HO")
ImmAckRequiredToken        = ("ImmAckRequired"         "IA")
InactiveToken              = ("Inactive"               "IN")
IsolateToken               = ("Isolate"                "IS")
InSvcToken                 = ("InService"              "IV")
InterruptByEventToken      = ("IntByEvent"             "IBE")
KeepActiveToken            = ("KeepActive"             "KA")
LocalToken                 = ("Local"                  "L")
LocalControlToken          = ("LocalControl"           "O")
LockStepToken              = ("LockStep"               "SP")
LoopbackToken              = ("Loopback"               "LB")
MediaToken                 = ("Media"                  "M")
MegacopToken = Literal("MEGACO") | Literal("!")
MethodToken                = ("Method"                 "MT")
MgcIdToken                 = ("MgcIdToTry"             "MG")
ModeToken                  = ("Mode"                   "MO")
ModifyToken                = ("Modify"                 "MF")
ModemToken                 = ("Modem"                  "MD")
MoveToken                  = ("Move"                   "MV")
MTPToken                   = ("MTP")
MuxToken                   = ("Mux"                    "MX")
NotifyToken                = ("Notify"                 "N")
NotifyCompletionToken      = ("NotifyCompletion"       "NC")
ObservedEventsToken        = ("ObservedEvents"         "OE")
OnewayToken                = ("Oneway"                 "OW")
OnOffToken                 = ("OnOff"                  "OO")
OtherReasonToken           = ("OtherReason"            "OR")
OutOfSvcToken              = ("OutOfService"           "OS")
PackagesToken              = ("Packages"               "PG")
PendingToken = Literal("Pending") | Literal("PN")
PriorityToken = Literal("Priority") | Literal("PR")
ProfileToken = Literal("Profile") | Literal("PF")
ReasonToken = Literal("Reason") | Literal("RE")
RecvonlyToken = Literal("ReceiveOnly") | Literal("RC")
ReplyToken = Literal("Reply") | Literal("P")
RestartToken = Literal("Restart") | Literal("RS")
RemoteToken = Literal("Remote") | Literal("R")
ReservedGroupToken = Literal("ReservedGroup") | Literal("RG")
ReservedValueToken = Literal("ReservedValue") | Literal("RV")
SendonlyToken = Literal("SendOnly") | Literal("SO")
SendrecvToken = Literal("SendReceive") | Literal("SR")
ServicesToken = Literal("Services") | Literal("SV")
ServiceStatesToken = Literal("ServiceStates") | Literal("SI")
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
LSBRKT = Literl("[")
RSBRKT = Literal("]")
EQUAL = Literal("=")
COLON = Literal(":")
SLASH = Literal("/")
COMMA = Literal(",")
octetString = printables
INEQUAL = Literal(">") | Literal("<") | Literal("#")
RestChar = "; [ ] { } : , # < > ="
Version = OneOrMore(nums)
COMMENT = ";" + Word(alphanums+"+ - & ! / \ ? @ ^ ` ~ * $ \( \) \" % \| .")
domainAddress = "[" + Combine(Word(nums,max=3) + ((".")+Word(nums,max=3))*3) + "]"
domainName = "<" + Combine(Word(alphanums)+Word(alphanums+"- .",max=63)) + ">"
portNumber = Word(nums)
mId = (domainAddress | domainName)+Optional(":"+portNumber)
message = MegacopToken + '/' + Version + mId 
authenticationHeader = AuthToken + "=" + "0x" + Word(hexnums,min=8,exact=8)+"0x"+Word(hexnums,min=8,max=8)+Word(hexnums,min=24,max=64)
megacoMessage = Optional(authenticationHeader) + message

TransactionID = Word(nums, max=32)
ContextID = Word(nums, max=32) | "*" | "-" | "$"
NAME = Word(alphas,min=1,max=1) + Word(alphanums + "_",max=63)
pathDomainName = Word(alphanums+"*",min=1,max=1) + Word(alphanums+"-",max=63)
pathNAME = Optional("*") + NAME + ZeroOrMore(Literal("|") | Literal("*") | alphanums | Literal("_") | Literal("$")) + Optional(Literal("@") + pathDomainName)
TerminationID = Literal("ROOT") | pathNAME | "$" | "*"


topologyDirection = BothwayToken | IsolateToken | OnewayToken
topologyTriple = TerminationID + "," + TerminationID + topologyDirection
topologyDescriptor = TopologyToken + "LBRKT" + delimitedList(topologyTriple) + "}"
priority = PriorityToken + "=" + Word(nums, max=16)
contextProperty = topologyDescriptor | priority | EmergencyToken
contextProperties = delimitedList(contextProperty)

contextAuditProperties = TopologyToken | EmergencyToken | PriorityToken
contextAudit = ContextAuditToken + "{" + delimitedList(contextAuditProperties) + "}"
contextRequest = contextAudit | (contextProperties + Optional("," + contextAudit))


notifyRequest = 
auditRequest = 
subtractRequest = 
RequestID = Word(nums,max=32) | "*"
StreamID = Word(nums,max=16)
signalListId = Word(nums,max=16)

pkgdName = (PackageName + SLASH + ItemID) | (PackageName + SLASH + Literal("*")) | (Literal("*") + SLASH + Literal("*"))
signalName = pkgdName
sigStream = StreamToken + EQUAL + StreamID
sigParameterName = NAME
sigOther = sigParameterName + parmValue
sigDuration = DurationToken + EQUAL + Word(nums,max=16)
signalType = OnOffToken | TimeOutToken | BriefToken
sigSignalType = SignalTypeToken + EQUAL + signalType
sigParameter = sigStream | sigSignalType | sigDuration | sigOther | notifyCompletion | KeepActiveToken
signalList = SignalListToken + EQUAL + signalListId + LBRKT + delimitedList(signalListParm) + RBRKT
signalRequest = signalName + LBRKT + delimitedList(sigParameter) + RBRKT
signalListParm = signalRequest
signalParm  = signalList | signalRequest
signalsDescriptor = SignalsToken + LBRKT + delimitedList(signalParm) + RBRKT
embedSig = EmbedToken + LBRKT + signalsDescriptor + RBRKT
eventStream = StreamToken + EQUAL + StreamID
eventParameterName = NAME
parmValue = (EQUAL + alternativeValue) | (INEQUAL + VALUE)
eventOther = eventParameterName + parmValue
eventDM = DigitMapToken + EQUAL + (digitMapName | (LBRKT + digitMapValue + RBRKT))
secondEventParameter = embedSig | KeepActiveToken | eventDM | eventStream | eventOther
secondRequestedEvent = pkgdName + Optional(LBRKT + delimitedList(secondEventParameter) + RBRKT)
embedFirst = EventsToken + Optional(EQUAL + RequestID + LBRKT + delimitedList(secondRequestedEvent) + RBRKT)
embedWithSig = EmbedToken + LBRKT + signalsDescriptor + Optional(COMMA + embedFirst) + RBRKT
embedNoSig = EmbedToken + LBRKT + embedFirst + RBRKT
eventParameter = embedWithSig | embedNoSig | KeepActiveToken | eventDM | eventStream | eventOther
requestedEvent = pkgdName + Optional(LBRKT + delimitedList(eventParameter) + RBRKT)
eventsDescriptor = EventsToken + Optional(EQUAL + RequestID + delimitedList(requestedEvent) + RBRKT)
ammParameter = mediaDescriptor | modemDescriptor | muxDescriptor | eventsDescriptor | signalsDescriptor | digitMapDescriptor | eventBufferDescriptor | auditDescriptor
ammRequest = (AddToken | MoveToken | ModifyToken ) + "=" + TerminationID + Optional(Literal("{")+delimitedList(ammParameter) + Literal("}"))
commandRequest = ammRequest | subtractRequest | auditRequest | notifyRequest | serviceChangeRequest
commandRequestList = Optional("O-") + Optional("W-") + commandRequest

ammsReply = (AddToken | MoveToken | ModifyToken | SubtractToken) + "=" + TerminationID + Optional(Literal("{") + terminationAudit + Literal("}"))
subtractRequest = SubtractToken + "=" + TerminationID + Optional(Literal("{") + auditDescriptor + Literal("}"))
auditRequest = (AuditValueToken | AuditCapToken) + "=" + TerminationID + "{" + auditDescriptor + "}"
terminationAudit = delimitedList(auditReturnParameter)
auditOther = "=" + TerminationID + Optional(Literal("{") + terminationAudit + Literal("}"))
contextTerminationAudit = "=" + CtxToken + (terminationIDList | (Literal("{") + errorDescriptor + Literal("}")))
auditReply = (AuditValueToken | AuditCapToken) + (contextTerminationAudit | auditOther)

auditDescriptor = AuditToken + "{" + Optional(delimitedList(auditItem)) + "}"
auditReturnParameter = mediaDescriptor | modemDescriptor | muxDescriptor | eventsDescriptor | signalsDescriptor | digitMapDescriptor | observedEventsDescriptor | eventBufferDescriptor | statisticsDescriptor | packagesDescriptor | errorDescriptor | auditItem
notifyRequest = NotifyToken + "=" + TerminationID + "{" + observedEventsDescriptor + Optional(Literal(",")+errorDescriptor) + "}"
notifyReply = NotifyToken + "=" + TerminationID + Optional(Literal("{") + errorDescriptor + Literal("}"))

serviceChangeRequest = ServiceChangeToken + "=" + TerminationID + "{" + serviceChangeDescriptor + "}"

quotedString = QuotedString('"')
ErrorCode = Word(nums,min=1,max=4)
errorDescriptor = ErrorToken + EQUAL + ErrorCode + LBRKT + Optional(quotedString) + RBRKT
serviceChangeReply = ServiceChangeToken + "=" + TerminationID + Optional(LBRKT + (errorDescriptor | serviceChangeReplyDescriptor) + RBRKT)

streamParm = localDescriptor | remoteDescriptor | localControlDescriptor
streamDescriptor = StreamToken + EQUAL + StreamID + LBRKT + delimitedList(streamParm) + RBRKT
reservedValueMode = ReservedValueToken + EQUAL + (Literal("ON") | Literal("OFF"))
reservedGroupMode = ReservedGroupToken + EQUAL + (Literal("ON") | Literal("OFF"))
localParm = streamMode | propertyParm | reservedValueMode | reservedGroupMode 
localControlDescriptor = LocalControlToken + LBRKT + delimitedList(localParm) + RBRKT
mediaParm = streamParm | streamDescriptor | terminationStateDescriptor
mediaDescriptor = MediaToken + LBRKT + delimitedList(mediaParm) + RBRKT



streamModes = SendonlyToken | RecvonlyToken | SendrecvToken | InactiveToken | LoopbackToken
streamMode = ModeToken + EQUAL + streamModes
VALUE = quotedString | Word(alphanums+"+ - & ! / \ ? @ ^ ` ~ * $ \( \) \" % \| .", min=1)
alternativeValue = VALUE | (LSBRKT + delimitedList(VALUE) + RSBRKT) | (LBRKT + delimitedList(VALUE) + RBRKT) | (LSBRKT + VALUE + COLON + VALUE + RSBRKT)
PackageName = NAME
ItemID = NAME
propertyParm = pkgdName + parmValue

localDescriptor = LocalToken + LBRKT + octetString + RBRKT
remoteDescriptor = RemoteToken + LBRKT + octetString + RBRKT
eventSpecParameter = eventStream | eventOther
eventSpec = pkgdName + Optional(LBRKT + delimitedList(eventSpecParameter) + RBRKT)
eventBufferDescriptor = EventBufferToken + Optional(LBRKT + delimitedList(eventSpec) + RBRKT)

eventBufferControl = BufferToken + EQUAL + (Literal("OFF") | LockStepToken)
serviceStates = ServiceStatesToken + EQUAL + (TestToken | OutOfSvcToken | InSvcToken)
terminationStateParm = propertyParm | serviceStates | eventBufferControl
terminationStateDescriptor = TerminationStateToken + LBRKT + delimitedList(terminationStateParm) + RBRKT

MuxType = H221Token | H223Token | H226Token | V76Token | extensionParameter
muxDescriptor = MuxToken + EQUAL + MuxType + terminationIDList





actionRequest = CtxToken + "=" + ContextID + "{" + ((contextRequest + Optional("," + commandRequestList)) | commandRequestList) + "}"

transactionPending = PendingToken + "=" + TransactionID + "{"
transactionAck = TransactionID | (TransactionID + "-" + TransactionID)
transactionResponseAck = ResponseAckToken + "{" + transactionAck
transactionRequest = TransToken + "=" + TransactionID + "{" + delimitedList(actionRequest) + "}"


actionReply = CtxToken + "=" + ContextID + "{" + ((errorDescriptor | commandReply) | (commandReply + "," + errorDescriptor)) + "}"
commandReplys = serviceChangeReply | auditReply | ammsReply | notifyReply
commandReplyList = delimitedList(commandReplys)
commandReply = commandReplyList | (contextProperties + Optional(Literal(",")+commandReplyList))

actionReplyList = delimitedList(actionReply)
transactionReply = 
transactionList = OneOrMore(transactionRequest | transactionReply | transactionPending | transactionResponseAck)
messageBody = errorDescriptor | transactionList
